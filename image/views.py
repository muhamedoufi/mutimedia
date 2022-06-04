import os
from django.shortcuts import render,redirect
from image.forms import NewImage
from django.urls import reverse
from django.contrib.auth.models import User
from image.models import Image
from django.contrib import messages

# Create your views here......

def imageform(request):
    if request.method == 'POST':
        patient_Form = NewImage(request.POST, request.FILES)
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


def updateImage(request,pk):
    Images=Image.objects.get(id=pk)
    form=NewImage(instance=Images)
    if request.method=="POST":
        #   print(request.POST)
        form=NewImage(request.POST,request.FILES,instance=Images)
        if form.is_valid():
            form.save()
            return(redirect('/images'))
    context={'image_Form':form}
    return render(request, 'image/imageform.html',context)


def deleteImage(request,pk):
    Images=Image.objects.get(id=pk)
    if request.method=="POST":
        Images.delete()
        return(redirect('/images'))
        
    context={'Imageform':Images}
    return render(request, 'image/deleteImage.html',context)
