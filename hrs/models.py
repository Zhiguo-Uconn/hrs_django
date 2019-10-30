from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone
from django.urls import reverse
from hrs.supports.drivenFactors import driven_factors

# Create your models here.
class Patient(models.Model):
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    race_choices = [
        ('W', 'White'),
        ('B', 'Black'),
        ('A', 'Asian'),
        ('H', 'Hispanic'),
        ('I', 'AI/AN'),
    ]

    firstName = models.CharField("First Name", max_length=30)
    lastName = models.CharField('Last Name', max_length=50)
    gender = models.CharField('Gender', max_length=1, choices=gender_choices)
    race = models.CharField('Race', max_length=1, choices=race_choices) 
    birthday=models.DateField('Date of Birth', default = '1970-01-01')
    doc = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name="Doctor")

    @property
    def age(self):
        today = date.today()
        birthday = self.birthday
        return(today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day)) )

    def get_absolute_url(self):
        return reverse('patient-detail', kwargs={'pk': self.pk})


class MedRecord(models.Model):
    #marital_choices = list(driven_factors.get("MaritalStatus").items())
    marital_choices = driven_factors.get('MaritalStatus')
    print(marital_choices)
    patient = models.ForeignKey(Patient,on_delete = models.CASCADE, verbose_name = "Patient" )
    a1c = models.DecimalField("A1c", max_digits=3, decimal_places=1)
    fastGlucose = models.DecimalField("Fast Glucose", max_digits=3, decimal_places=1)
    recordTime = models.DateTimeField(default = timezone.now)
    MaritalStatus = models.CharField('Marital Status', max_length=50, choices=marital_choices)
