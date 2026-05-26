from django.db import models


class DiseaseAdvisory(models.Model):
    """
    Stores advisory information for each plant disease.
    disease_key matches exactly with CLASS_NAMES from
    class_mapping.json
    Example key: 'Tomato___Early_blight'
    """
    disease_key = models.CharField(
        max_length=200,
        unique=True,
        help_text='Matches class name from AI model'
    )
    disease_name = models.CharField(max_length=200)
    plant = models.CharField(max_length=100)
    disease = models.CharField(max_length=100)
    is_healthy = models.BooleanField(default=False)

    # Disease details
    symptoms = models.TextField(
        help_text='Visual symptoms on leaves/plant'
    )
    causes = models.TextField(
        help_text='Fungal/bacterial/viral causes'
    )

    # Treatment
    organic_treatment = models.TextField(
        help_text='Natural and organic remedies'
    )
    chemical_treatment = models.TextField(
        help_text='Chemical fungicides/pesticides'
    )
    prevention = models.TextField(
        help_text='Prevention and control methods'
    )

    # Severity and urgency
    severity_level = models.CharField(
        max_length=20,
        choices=[
            ('Low', 'Low'),
            ('Medium', 'Medium'),
            ('Severe', 'Severe'),
            ('Healthy', 'Healthy'),
        ],
        default='Medium'
    )
    urgency_message = models.CharField(
        max_length=300,
        blank=True,
        help_text='Short urgent action message'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['plant', 'disease']
        verbose_name = 'Disease Advisory'
        verbose_name_plural = 'Disease Advisories'

    def __str__(self):
        return f"{self.plant} - {self.disease}"

    @staticmethod
    def _as_list(value):
        return [line.strip() for line in value.splitlines() if line.strip()]

    @property
    def crop_host(self):
        return self.plant

    @property
    def severity(self):
        return self.severity_level

    @property
    def description(self):
        return self.causes

    @property
    def causative_agent(self):
        return self.causes

    @property
    def pathogen(self):
        return 'Plant disease'

    @property
    def primary_symptoms(self):
        return self.symptoms

    @property
    def preventative_culturing(self):
        return self.prevention

    @property
    def chemical_controls(self):
        return self.chemical_treatment

    def get_primary_symptoms_list(self):
        return self._as_list(self.symptoms) or [self.symptoms]

    def get_preventative_culturing_list(self):
        return self._as_list(self.prevention) or [self.prevention]

    def get_organic_treatment_list(self):
        return self._as_list(self.organic_treatment) or [self.organic_treatment]

    def get_chemical_controls_list(self):
        return self._as_list(self.chemical_treatment) or [self.chemical_treatment]
