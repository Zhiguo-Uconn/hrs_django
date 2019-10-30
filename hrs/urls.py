from django.urls import path
from . import views

urlpatterns = [
    path('', views.patientSearch, name='hrs-home'),
    path('patients/', views.PatientListView.as_view(), name='patients'),
    path('patients/<int:pk>', views.PatientDetailView.as_view(), name='patient-detail'),
    path('patients/pid=<int:pid>', views.patientDetail, name='patient-detail-test'),
    path('about/', views.about, name='hrs-about'),
    path('hrs/new/', views.PatientCreateView.as_view(), name='patient-new'),
    path('hrs/search/', views.patientSearch, name='patient-search'),
    path('hrs/patients/pid=<int:pid>/medRecord/', views.mrCreateView, name='patient-medRecord'),
]