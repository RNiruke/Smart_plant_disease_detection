from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from django.views.decorators.http import require_POST

from .models import DiseaseAdvisory


# ── PUBLIC ADVISORY VIEWS ────────────────────────────────────────────────────

@login_required
def advisory_list_view(request):
    """Show all plant advisories grouped by plant."""
    plants = DiseaseAdvisory.objects.values_list(
        'plant', flat=True
    ).distinct().order_by('plant')

    advisories = DiseaseAdvisory.objects.all().order_by(
        'plant', 'disease'
    )

    return render(request, 'advisory/advisory_list.html', {
        'advisories': advisories,
        'plants': plants,
        'title': 'Crop Advisory'
    })


@login_required
def advisory_detail_view(request, disease_key):
    """Show detailed advisory for a specific disease."""
    lookup = Q(disease_key=disease_key)
    if disease_key.isdigit():
        lookup |= Q(pk=int(disease_key))

    advisory = get_object_or_404(
        DiseaseAdvisory,
        lookup
    )
    return render(request, 'advisory/detail.html', {
        'advisory': advisory,
        'title': f'{advisory.plant} - {advisory.disease}'
    })


def get_advisory_for_detection(disease_key):
    """
    Helper function called from detector views.
    Returns advisory object or None if not found.
    """
    try:
        advisory = DiseaseAdvisory.objects.get(
            disease_key=disease_key
        )
        return advisory
    except DiseaseAdvisory.DoesNotExist:
        return None


# ── ADMIN PANEL — CRUD (preserve existing admin functionality) ───────────────

@staff_member_required(login_url='/accounts/login/')
def advisory_admin_table(request):
    """
    Custom admin management table — lists all DiseaseAdvisory records.
    Staff / superuser only.
    """
    diseases = DiseaseAdvisory.objects.all().order_by('plant', 'disease')
    success = request.session.pop('advisory_success', None)
    return render(request, 'advisory/admin_table.html', {
        'diseases': diseases,
        'success': success,
        'title': 'Advisory Disease Management',
    })


@staff_member_required(login_url='/accounts/login/')
def advisory_admin_add(request):
    """
    Add a new DiseaseAdvisory record (GET: show form, POST: save).
    """
    if request.method == 'POST':
        try:
            DiseaseAdvisory.objects.create(
                disease_key=request.POST.get('disease_key', '').strip(),
                disease_name=request.POST.get('disease_name', '').strip(),
                plant=request.POST.get('plant', '').strip(),
                disease=request.POST.get('disease', '').strip(),
                is_healthy=request.POST.get('is_healthy') == 'on',
                symptoms=request.POST.get('symptoms', '').strip(),
                causes=request.POST.get('causes', '').strip(),
                organic_treatment=request.POST.get('organic_treatment', '').strip(),
                chemical_treatment=request.POST.get('chemical_treatment', '').strip(),
                prevention=request.POST.get('prevention', '').strip(),
                severity_level=request.POST.get('severity_level', 'Medium'),
                urgency_message=request.POST.get('urgency_message', '').strip(),
            )
            messages.success(request, 'Disease module added successfully. ✓')
            return redirect('advisory:admin_table')
        except Exception as e:
            return render(request, 'advisory/admin_form.html', {
                'form_mode': 'add',
                'title': 'Add Disease Module',
                'disease': None,
                'post_data': request.POST,
                'error': str(e),
            })

    return render(request, 'advisory/admin_form.html', {
        'form_mode': 'add',
        'title': 'Add Disease Module',
        'disease': None,
    })


@staff_member_required(login_url='/accounts/login/')
def advisory_admin_edit(request, pk):
    """
    Edit an existing DiseaseAdvisory record (GET: prefilled form, POST: update).
    """
    disease = get_object_or_404(DiseaseAdvisory, pk=pk)

    if request.method == 'POST':
        try:
            disease.disease_key = request.POST.get('disease_key', '').strip()
            disease.disease_name = request.POST.get('disease_name', '').strip()
            disease.plant = request.POST.get('plant', '').strip()
            disease.disease = request.POST.get('disease', '').strip()
            disease.is_healthy = request.POST.get('is_healthy') == 'on'
            disease.symptoms = request.POST.get('symptoms', '').strip()
            disease.causes = request.POST.get('causes', '').strip()
            disease.organic_treatment = request.POST.get('organic_treatment', '').strip()
            disease.chemical_treatment = request.POST.get('chemical_treatment', '').strip()
            disease.prevention = request.POST.get('prevention', '').strip()
            disease.severity_level = request.POST.get('severity_level', 'Medium')
            disease.urgency_message = request.POST.get('urgency_message', '').strip()
            disease.save()
            messages.success(request, 'Disease module updated successfully. ✓')
            next_url = request.POST.get('next') or 'advisory:admin_table'
            return redirect(next_url)
        except Exception as e:
            return render(request, 'advisory/admin_form.html', {
                'form_mode': 'edit',
                'title': 'Edit Disease Module',
                'disease': disease,
                'post_data': request.POST,
                'error': str(e),
            })

    return render(request, 'advisory/admin_form.html', {
        'form_mode': 'edit',
        'title': 'Edit Disease Module',
        'disease': disease,
    })


@staff_member_required(login_url='/accounts/login/')
@require_POST
def advisory_admin_delete(request, pk):
    """
    Delete a DiseaseAdvisory record by ID.
    """
    disease = get_object_or_404(DiseaseAdvisory, pk=pk)
    disease.delete()
    messages.success(request, 'Disease deleted successfully')
    next_url = request.POST.get('next') or 'advisory:admin_table'
    return redirect(next_url)
