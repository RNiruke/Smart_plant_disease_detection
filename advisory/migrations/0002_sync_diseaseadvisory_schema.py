# Generated manually to align the existing advisory table with the current model.

from django.db import migrations, models


def populate_new_fields(apps, schema_editor):
    DiseaseAdvisory = apps.get_model('advisory', 'DiseaseAdvisory')
    for advisory in DiseaseAdvisory.objects.all().order_by():
        plant = getattr(advisory, 'plant', '') or 'Unknown'
        disease_name = getattr(advisory, 'disease_name', '') or 'Unknown'
        disease = disease_name
        disease_key = f"{plant}___{disease_name}".replace(' ', '_')

        advisory.disease = disease
        advisory.disease_key = disease_key
        advisory.is_healthy = 'healthy' in disease_name.lower()
        advisory.save(update_fields=['disease', 'disease_key', 'is_healthy'])


class Migration(migrations.Migration):

    dependencies = [
        ('advisory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diseaseadvisory',
            old_name='crop_host',
            new_name='plant',
        ),
        migrations.RenameField(
            model_name='diseaseadvisory',
            old_name='severity',
            new_name='severity_level',
        ),
        migrations.RenameField(
            model_name='diseaseadvisory',
            old_name='primary_symptoms',
            new_name='symptoms',
        ),
        migrations.RenameField(
            model_name='diseaseadvisory',
            old_name='description',
            new_name='causes',
        ),
        migrations.RenameField(
            model_name='diseaseadvisory',
            old_name='preventative_culturing',
            new_name='prevention',
        ),
        migrations.RenameField(
            model_name='diseaseadvisory',
            old_name='chemical_controls',
            new_name='chemical_treatment',
        ),
        migrations.AddField(
            model_name='diseaseadvisory',
            name='disease_key',
            field=models.CharField(
                help_text='Matches class name from AI model',
                max_length=200,
                null=True,
                unique=True,
            ),
        ),
        migrations.AddField(
            model_name='diseaseadvisory',
            name='disease',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diseaseadvisory',
            name='is_healthy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='diseaseadvisory',
            name='urgency_message',
            field=models.CharField(
                blank=True,
                help_text='Short urgent action message',
                max_length=300,
            ),
        ),
        migrations.RunPython(populate_new_fields, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='diseaseadvisory',
            name='disease_key',
            field=models.CharField(
                help_text='Matches class name from AI model',
                max_length=200,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name='diseaseadvisory',
            name='severity_level',
            field=models.CharField(
                choices=[
                    ('Low', 'Low'),
                    ('Medium', 'Medium'),
                    ('Severe', 'Severe'),
                    ('Healthy', 'Healthy'),
                ],
                default='Medium',
                max_length=20,
            ),
        ),
        migrations.RemoveField(
            model_name='diseaseadvisory',
            name='causative_agent',
        ),
        migrations.RemoveField(
            model_name='diseaseadvisory',
            name='pathogen',
        ),
        migrations.AlterModelOptions(
            name='diseaseadvisory',
            options={
                'ordering': ['plant', 'disease'],
                'verbose_name': 'Disease Advisory',
                'verbose_name_plural': 'Disease Advisories',
            },
        ),
    ]
