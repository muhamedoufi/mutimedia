import os
from django.shortcuts import render,redirect
from image.forms import NewImage
from django.urls import reverse
from django.contrib.auth.models import User
from image.models import Image
from django.contrib import messages

# Create your views here.

def imageform(request):
    if request.method == 'POST':
        patient_Form = NewImage(request.POST)
        if patient_Form.is_valid():
            patient_Form= patient_Form.save(commit=False)
            patient_Form.technicien = User.objects.get(id=request.user.id)
            myform = patient_Form.save()
            messages.success( 
                # {myform.nom}/{myform.prenom}
                request, f"Felicitations l'image {patient_Form.img} est bien ajoutée")
            return redirect(reverse('image:imageform'))
    else:
        image_Form = NewImage()
        context={
           
            'image_Form' : image_Form,

        }
        return render(request,'image/imageform.html',context)


def showImages(request):
    context={

        'title': 'la Liste des Patient' ,
        'listimage': Image.objects.all(),

    }
    return render(request, 'image/images.html',context)
