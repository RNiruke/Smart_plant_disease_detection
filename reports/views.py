"""
Reports views — live diagnosis log tracking, filters, and reports export.
"""

import csv
import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

from detector.models import DiseaseDetection


@login_required
def history_list(request):
    """Lists history records with support for crop name and severity filters."""
    severity_filter = request.GET.get('severity', '').strip()
    crop_filter = request.GET.get('crop', '').strip()
    
    detections = DiseaseDetection.objects.filter(user=request.user)
    
    if severity_filter:
        db_severity = severity_filter
        if severity_filter == 'Moderate':
            db_severity = 'Medium'
        elif severity_filter == 'None':
            db_severity = 'Healthy'
        detections = detections.filter(severity=db_severity)
        
    if crop_filter:
        detections = detections.filter(plant__icontains=crop_filter)
        
    detections = detections.order_by('-timestamp')
    total = detections.count()
    
    return render(request, 'reports/history.html', {
        'detections': detections,
        'title': 'Detection History',
        'severity_filter': severity_filter,
        'crop_filter': crop_filter,
        'total': total,
    })


@login_required
def delete_detection(request, pk):
    """Securely deletes a diagnosis record and removes its uploaded leaf image from disk."""
    detection = get_object_or_404(DiseaseDetection, pk=pk, user=request.user)
    if request.method == 'POST':
        # Delete image file from media storage
        if detection.image:
            if os.path.isfile(detection.image.path):
                try:
                    os.remove(detection.image.path)
                except Exception as e:
                    # Log exception if file deletion fails but proceed with DB delete
                    pass
        detection.delete()
        messages.success(request, 'Detection record deleted successfully.')
    return redirect('reports:history')


@login_required
def download_report(request):
    """Exports user's diagnosis history logs as a downloadable CSV spreadsheet."""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="diagnoses_report.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'Scan ID', 'Crop / Host', 'Diagnosed Disease', 
        'Confidence Score (%)', 'Severity Level', 'Healthy Flag', 
        'Timestamp'
    ])

    detections = DiseaseDetection.objects.filter(user=request.user).order_by('-timestamp')
    for d in detections:
        writer.writerow([
            d.id, 
            d.plant.capitalize() if d.plant else "Unknown", 
            d.disease, 
            d.confidence, 
            d.severity, 
            d.is_healthy, 
            d.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        ])

    return response
