from django import forms
from .models import *
# from client.models import Client
# from django.contrib.auth import User
from crispy_forms.helper import FormHelper
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class NewPatient(forms.ModelForm):
    class Meta:
        model = Patient
        fields ='__all__' 
        exclude=['secretaire']
        widgets={
            "dateNaissance": DateInput()
        }

class NewConsultation(forms.ModelForm):
    class Meta:
        model = Consultation
        fields ='__all__' 
        exclude=['medecin']
        widgets={
            "dateConsultation": DateInput()
        }

class NewRendevous(forms.ModelForm):
    class Meta:
        model = Rendevous
        fields ='__all__' 
        widgets={
            "dateRendevou": DateInput()
        }