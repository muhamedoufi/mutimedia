from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib import messages
from patient.forms import NewPatient
from django.urls import reverse
from django.contrib.auth.models import User
from .decorators import *
from patient.models import Patient

# Create your views here.

def home(request):
    return render(request, 'patient/homePage.html', {"title": "home"})

def contact(request):
    return render(request, 'patient/contact.html', {"title": "home"})

def patientform(request):
    if request.method == 'POST':
        patient_Form = NewPatient(request.POST)
        if patient_Form.is_valid():
            patient_Form= patient_Form.save(commit=False)
            patient_Form.secretaire = User.objects.get(id=request.user.id)
            myform = patient_Form.save()
            messages.success( 
                # {myform.nom}/{myform.prenom}
                request, f"Felicitations le Patient {patient_Form.nom}/{patient_Form.prenom} est bien ajoutée")
            return redirect(reverse('patient:patientform'))
    else:
        patient_Form = NewPatient()
        context={
           
            'patient_Form' : patient_Form,

        }
        return render(request,'patient/patientform.html',context)
# @secretaire_only
def listPatient(request):
    print(request.user)
    print(request.user.groups.all()[0].name)
    context={

        'title': 'la Liste des Patient' ,
        'listPatient': Patient.objects.filter(secretaire=request.user),

    }
    return render(request,'patient/listPatient.html',context)

