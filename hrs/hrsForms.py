from django import forms
from .models import MedRecord


class MedRecordForm(forms.ModelForm):
    class Meta:
        model = MedRecord
        fields = '__all__'
        widgets = {
            'patient': forms.HiddenInput()
        }
        #exclude = ('patient', )