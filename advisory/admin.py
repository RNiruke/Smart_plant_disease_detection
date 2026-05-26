from django.contrib import admin
from .models import DiseaseAdvisory


@admin.register(DiseaseAdvisory)
class DiseaseAdvisoryAdmin(admin.ModelAdmin):
    list_display = [
        'plant', 'disease', 'severity_level',
        'is_healthy', 'updated_at'
    ]
    list_filter = ['plant', 'severity_level', 'is_healthy']
    search_fields = ['plant', 'disease', 'disease_key']
    ordering = ['plant', 'disease']
