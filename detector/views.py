import json
import os
import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseForbidden

from .models import DiseaseDetection
from .forms import ImageUploadForm
from utils.ai_pipeline import predict_disease
from utils.severity import get_severity, get_severity_color, get_severity_icon
from utils.image_utils import get_image_hash
from advisory.views import get_advisory_for_detection

@login_required
def upload_view(request):
    form = ImageUploadForm()
    
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES['image']
            
            # Generate hash for deduplication
            image_hash = get_image_hash(image_file)
            
            # Check if this user already uploaded this exact image
            existing = DiseaseDetection.objects.filter(
                user=request.user,
                image_hash=image_hash
            ).first()
            
            if existing:
                # Duplicate found - reuse existing result
                messages.info(
                    request,
                    f'You already analyzed this image. '
                    f'Showing your previous result.'
                )
                return redirect('detector:result', pk=existing.pk)
            
            # New image - save and predict
            detection = DiseaseDetection(
                user=request.user,
                image_hash=image_hash
            )
            detection.image = image_file
            detection.save()
            
            # Run AI prediction
            result = predict_disease(detection.image.path)
            
            if result['success']:
                detection.disease_name = result['class_name']
                detection.plant = result['plant']
                detection.disease = result['disease']
                detection.confidence = result['confidence']
                detection.is_healthy = result['is_healthy']
                detection.severity = get_severity(
                    result['confidence'], 
                    result['is_healthy']
                )
                detection.top3_json = json.dumps(result['top3'])
                detection.save()
                return redirect('detector:result', pk=detection.pk)
            else:
                # Prediction failed - delete saved image
                detection.image.delete(save=False)
                detection.delete()
                form.add_error(None, f"Prediction failed: {result['error']}")
    
    return render(request, 'detector/upload.html', {
        'form': form,
        'title': 'Upload Plant Leaf'
    })


@login_required
def result_view(request, pk):
    detection = get_object_or_404(
        DiseaseDetection, 
        pk=pk, 
        user=request.user
    )
    
    # Parse top3 JSON
    try:
        top3 = json.loads(detection.top3_json)
    except:
        top3 = []
    
    severity_color = get_severity_color(detection.severity)
    severity_icon = get_severity_icon(detection.severity)
    
    # Advisory lookup
    advisory = get_advisory_for_detection(detection.disease_name)
    
    return render(request, 'detector/result.html', {
        'detection': detection,
        'top3': top3,
        'advisory': advisory,
        'severity_color': severity_color,
        'severity_icon': severity_icon,
        'title': 'Detection Result'
    })


@login_required
def history_view(request):
    detections = DiseaseDetection.objects.filter(
        user=request.user
    ).order_by('-timestamp')
    
    paginator = Paginator(detections, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'detector/history.html', {
        'page_obj': page_obj,
        'title': 'Detection History'
    })


@login_required
def delete_view(request, pk):
    detection = get_object_or_404(
        DiseaseDetection,
        pk=pk,
        user=request.user
    )
    if request.method == 'POST':
        # Delete image file from media
        if detection.image:
            if os.path.isfile(detection.image.path):
                os.remove(detection.image.path)
        detection.delete()
        messages.success(request, 'Detection record deleted successfully.')
        return redirect('detector:history')
    return HttpResponseForbidden()


@login_required
def download_view(request):
    """
    Exports diagnosis history logs as a downloadable CSV spreadsheet.
    """
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
            d.id, d.plant, d.disease, 
            d.confidence, d.severity, d.is_healthy, 
            d.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        ])

    return response
