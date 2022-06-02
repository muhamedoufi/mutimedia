from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib import messages
from patient.forms import NewPatient,NewConsultation,NewRendevous
from django.urls import reverse
from django.contrib.auth.models import User
from .decorators import *
from patient.models import Patient,Consultation,Rendevous

# Create your views here.

def home(request):

    return render(request, 'patient/homePage.html', {"title": "home",})

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

def consultation(request):
    if request.method == 'POST':
        consultation_Form = NewConsultation(request.POST)
        if consultation_Form.is_valid():
            consultation_Form = consultation_Form.save(commit=False)
            consultation_Form.medecin = User.objects.get(id=request.user.id)
            myform = consultation_Form.save()
            messages.success( 
                # {myform.nom}/{myform.prenom}
                request, f"Felicitations la consultation de la Patient {consultation_Form.patient.nom}est bien ajoutée")
            return redirect(reverse('patient:consultation'))
    else:
        consultation_Form = NewConsultation()
        context={
           
            'consultation_Form' : consultation_Form,

        }
        return render(request,'patient/consultation.html',context)

def listConsultation(request):
    print(request.user)
    print(request.user.groups.all()[0].name)
    context={

        'title': 'la Liste des Consultations' ,
        'listConsultation': Consultation.objects.filter(medecin=request.user),

    }
    return render(request,'patient/listConsultation.html',context)


def rendevous(request):
    if request.method == 'POST':
        rendevous_Form = NewRendevous(request.POST)
        if rendevous_Form.is_valid():
            rendevous_Form = rendevous_Form.save(commit=False)
            # rendevous_Form.medecin = User.objects.get(id=request.user.id)
            myform = rendevous_Form.save()
            messages.success( 
                # {myform.nom}/{myform.prenom}
                request, f"Felicitations un Rendevous pour le Patient  {rendevous_Form.patient} est bien planifié")
            return redirect(reverse('patient:rendevous'))
    else:
        rendevous_Form = NewRendevous()
        context={
           
            'rendevous_Form' : rendevous_Form,

        }
        return render(request,'patient/rendevous.html',context)

def listRendevous(request):
    context = {}
    if request.user.groups.all()[0].name == 'medecins':
        context={

            'title': 'la Liste des Rendevous' ,
            'listRendevous': Rendevous.objects.filter(medecin_technicien=request.user),

        }
    elif request.user.groups.all()[0].name == 'secretaires':
        context={

            'title': 'la Liste des Rendevous' ,
            'listRendevous': Rendevous.objects.all(),

        }
    elif request.user.groups.all()[0].name == 'techniciens':
        context={

            'title': 'la Liste des Rendevous' ,
            'listRendevous': Rendevous.objects.filter(medecin_technicien=request.user),

        }
    else :
        context = {}
    return render(request,'patient/listRendevous.html',context)

def imprimer_Rendevous(request, id):
    rendevous = Rendevous.objects.get(id=id)
   
    return render(request,'patient/imprimer_Rendevous.html',{'rendevous':  rendevous})

