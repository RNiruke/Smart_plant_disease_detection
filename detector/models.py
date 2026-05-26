from django.db import models
from django.conf import settings

class DiseaseDetection(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='detections'
    )
    image = models.ImageField(upload_to='uploads/')
    image_hash = models.CharField(
        max_length=32, 
        blank=True, 
        null=True,
        help_text='MD5 hash for duplicate detection'
    )
    disease_name = models.CharField(max_length=200)
    plant = models.CharField(max_length=100, blank=True)
    disease = models.CharField(max_length=100, blank=True)
    confidence = models.FloatField(default=0.0)
    severity = models.CharField(max_length=20, blank=True)
    is_healthy = models.BooleanField(default=False)
    top3_json = models.TextField(blank=True, default='[]')
    timestamp = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.user.username} - {self.disease_name} - {self.timestamp}"

    @property
    def created_at(self):
        return self.timestamp

    @property
    def crop_name(self):
        return self.plant.capitalize() if self.plant else "Unknown"

    @property
    def severity_badge(self):
        return {
            'Healthy': 'success',
            'Low': 'info',
            'Medium': 'warning',
            'Moderate': 'warning',
            'Severe': 'danger',
        }.get(self.severity, 'secondary')
