from django.contrib import admin
from .models import DiseaseDetection

@admin.register(DiseaseDetection)
class DiseaseDetectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'plant', 'disease', 'confidence', 'severity', 'is_healthy', 'timestamp')
    list_filter = ('severity', 'is_healthy', 'plant', 'timestamp')
    search_fields = ('user__username', 'plant', 'disease')
    ordering = ('-timestamp',)
