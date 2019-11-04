from django.shortcuts import render, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView
from .models import Patient, MedRecord
from django.db.models import Q, Count
from django.core.exceptions import ValidationError
from .hrsForms import MedRecordForm
from . import calculation

# Create your views here.
@login_required
def home(request):
    return render(request, 'hrs/home.html')

@login_required
def about(request):
    patient = Patient.objects.get(pk=2)
    test_hrs = calculation.get_hle(1, patient)
  
    mr = MedRecord.objects.get(pk=1)

    return render(request, 'hrs/about.html', context={'HLE': test_hrs, 'mr': mr})


class PatientListView(ListView):
    model = Patient
    template_name = 'hrs/patients.html'
    context_object_name = 'patients'
    ordering = ['lastName']


def patientDetail(request, pid):
    patient = Patient.objects.get(pk=pid)
    medRecord = MedRecord.objects.filter(patient = patient).last()
    
    context = {
        'object': patient,
        'medRecord': medRecord,
    }
    return render(request, 'hrs/patient_detail.html', context)

class PatientDetailView(DetailView):
    model = Patient
    

class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    fields = '__all__'

    def form_valid(self, form):
        form.instance.doc = self.request.user
        return super().form_valid(form)


@login_required
def patientSearch(request):
    qs = filter(request)
    context = {
        'queryset': qs,
        'patients': Patient.objects.all()[:5]
    }
    
    return render(request, 'hrs/search.html', context)


def mrCreateView(request, pid):
    if request.method == 'POST':
        postForm = MedRecordForm(request.POST)
        print(postForm)
        if postForm.is_valid():
            postForm.save()
            return redirect('patient-detail', pid=pid)

    patient = Patient.objects.get(pk=pid)
    medRecord = MedRecord(patient = patient)
    mr_form = MedRecordForm(instance=medRecord)
    
    context = {
            'form': mr_form,
            'pid': pid,
        }
    
    return render(request, 'hrs/medRecord_form.html', context)


def filter(request):
    qs = Patient.objects.all()
    firstName_query = request.GET.get('firstName')
    lastName_query = request.GET.get('lastName')
    birthdate_query = request.GET.get('DOB')
    
    if is_valid_queryparam(firstName_query):
        qs =qs.filter(firstName__icontains=firstName_query)
    if is_valid_queryparam(lastName_query):
        qs =qs.filter(lastName__icontains=lastName_query)
    if is_valid_queryparam(birthdate_query):
        qs =qs.filter(birthday=birthdate_query)
    return qs

def is_valid_queryparam(param):
    try:
        return param != '' and param is not None
    except ValidationError:
        return False
    