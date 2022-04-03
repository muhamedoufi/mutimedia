from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from django import forms


class NewImage(forms.ModelForm):
    class Meta:
        model = Image
        fields ='__all__' 
        exclude=['technicien']
        