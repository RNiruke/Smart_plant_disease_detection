"""
Dashboard views — landing page, user dashboard, admin analytics.
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.db.models import Count, Avg, Q
from django.utils import timezone
from datetime import timedelta
import json

from detector.models import DiseaseDetection


def landing_page(request):
    """Public landing page."""
    return render(request, 'landing.html', {'title': 'Smart Plant Disease Detection'})


@login_required
def home(request):
    """User dashboard — shows stats and recent activity."""
    user = request.user
    if user.is_staff or user.is_superuser:
        return redirect('dashboard:analytics')
    detections = DiseaseDetection.objects.filter(user=user)
    
    total = detections.count()
    healthy = detections.filter(is_healthy=True).count()
    diseased = total - healthy
    severe = detections.filter(severity='Severe').count()
    
    # Latest 3 detections for recent activity list
    recent = detections.order_by('-timestamp')[:3]
    
    # Top Diseases (excluding Healthy) - Limit to top 5 for bar chart
    top_diseases = (
        detections.exclude(is_healthy=True)
        .values('disease')
        .annotate(count=Count('id'))
        .order_by('-count')[:5]
    )
    chart_labels = [item['disease'] for item in top_diseases]
    chart_data = [item['count'] for item in top_diseases]
    
    # Severity breakdown donut: ['Severe', 'Moderate', 'Low', 'Healthy']
    severe_cnt = detections.filter(severity='Severe').count()
    medium_cnt = detections.filter(severity__in=['Medium', 'Moderate']).count()
    low_cnt = detections.filter(severity='Low').count()
    healthy_cnt = healthy
    
    severity_data = [severe_cnt, medium_cnt, low_cnt, healthy_cnt]
    
    context = {
        'title': 'My Dashboard',
        'total': total,
        'healthy': healthy,
        'diseased': diseased,
        'severe': severe,
        'recent': recent,
        'chart_labels': json.dumps(chart_labels),
        'chart_data': json.dumps(chart_data),
        'severity_data': json.dumps(severity_data),
    }
    return render(request, 'dashboard/home.html', context)


def is_admin(user):
    return user.is_staff or user.is_superuser


@login_required
@user_passes_test(is_admin)
def admin_analytics(request):
    """Admin-only analytics dashboard with interactive user management and detailed charts."""
    User = get_user_model()
    
    # Handle user management actions via POST
    if request.method == 'POST':
        action = request.POST.get('action')
        target_user_id = request.POST.get('user_id')
        
        if action and target_user_id:
            try:
                target_user = User.objects.get(id=target_user_id)
                # Prevent self-editing
                if target_user == request.user:
                    messages.error(request, "You cannot modify your own active status or admin status.")
                elif action == 'toggle_status':
                    target_user.is_active = not target_user.is_active
                    target_user.save()
                    status_str = "activated" if target_user.is_active else "suspended"
                    messages.success(request, f"User '{target_user.username}' has been successfully {status_str}.")
                elif action == 'toggle_role':
                    target_user.is_staff = not target_user.is_staff
                    target_user.save()
                    role_str = "promoted to Administrator" if target_user.is_staff else "demoted to regular user"
                    messages.success(request, f"User '{target_user.username}' has been successfully {role_str}.")
            except User.DoesNotExist:
                messages.error(request, "Selected user does not exist.")
            
            return redirect('dashboard:analytics')

    # Global counters
    total_users = User.objects.count()
    active_users = User.objects.filter(is_active=True).count()
    suspended_users = User.objects.filter(is_active=False).count()
    staff_users = User.objects.filter(is_staff=True).count()
    
    all_detections = DiseaseDetection.objects.all()
    total_detections = all_detections.count()
    
    # Healthy vs Diseased
    healthy_count = all_detections.filter(is_healthy=True).count()
    diseased_count = total_detections - healthy_count
    
    avg_confidence = all_detections.aggregate(Avg('confidence'))['confidence__avg'] or 0
    avg_confidence = round(avg_confidence, 2)
    
    # Recent Uploads (last 8 scans across all users)
    recent_uploads = all_detections.select_related('user').order_by('-timestamp')[:8]
    
    # Top Diseases (excluding Healthy) - Limit to top 5
    top_diseases_qs = (
        all_detections.exclude(is_healthy=True)
        .values('disease', 'plant')
        .annotate(count=Count('id'))
        .order_by('-count')[:5]
    )
    
    top_diseases = []
    for item in top_diseases_qs:
        top_diseases.append({
            'disease_name': item['disease'],
            'crop_name': item['plant'].capitalize() if item['plant'] else "Unknown",
            'count': item['count']
        })

    # Severity distribution
    severe_cnt = all_detections.filter(severity='Severe').count()
    medium_cnt = all_detections.filter(severity__in=['Medium', 'Moderate']).count()
    low_cnt = all_detections.filter(severity='Low').count()
    healthy_cnt = healthy_count
    
    severity_data = [severe_cnt, medium_cnt, low_cnt, healthy_cnt]
    severity_labels = ['Severe', 'Moderate', 'Low', 'Healthy']

    # Crop scan volume breakdown (top 6 crops)
    crop_volume_qs = (
        all_detections.values('plant')
        .annotate(count=Count('id'))
        .order_by('-count')[:6]
    )
    crop_labels = [item['plant'].capitalize() if item['plant'] else "Unknown" for item in crop_volume_qs]
    crop_data = [item['count'] for item in crop_volume_qs]

    # Scans daily count over last 7 days
    labels, counts = [], []
    for i in range(6, -1, -1):
        day = timezone.now().date() - timedelta(days=i)
        labels.append(day.strftime('%b %d'))
        day_count = all_detections.filter(timestamp__date=day).count()
        counts.append(day_count)

    # User Directory: Search and Filters
    q = request.GET.get('q', '').strip()
    status_filter = request.GET.get('status', '').strip()
    
    users_qs = User.objects.annotate(
        detection_count=Count('detections')
    ).order_by('-date_joined')
    
    if q:
        users_qs = users_qs.filter(
            Q(username__icontains=q) |
            Q(email__icontains=q) |
            Q(first_name__icontains=q) |
            Q(last_name__icontains=q)
        )
        
    if status_filter == 'active':
        users_qs = users_qs.filter(is_active=True)
    elif status_filter == 'inactive':
        users_qs = users_qs.filter(is_active=False)
    elif status_filter == 'staff':
        users_qs = users_qs.filter(is_staff=True)
        
    context = {
        'title': 'Admin Analytics',
        'total_users': total_users,
        'active_users': active_users,
        'suspended_users': suspended_users,
        'staff_users': staff_users,
        'total_detections': total_detections,
        'healthy_count': healthy_count,
        'diseased_count': diseased_count,
        'avg_confidence': avg_confidence,
        'recent_uploads': recent_uploads,
        'top_diseases': top_diseases,
        'trend_labels': json.dumps(labels),
        'trend_data': json.dumps(counts),
        'severity_data': json.dumps(severity_data),
        'severity_labels': json.dumps(severity_labels),
        'crop_labels': json.dumps(crop_labels),
        'crop_data': json.dumps(crop_data),
        'users_list': users_qs,
        'q': q,
        'status_filter': status_filter,
    }
    return render(request, 'dashboard/admin_analytics.html', context)
