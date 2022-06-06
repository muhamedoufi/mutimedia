from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    secretaire = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    nom = models.CharField(max_length=45)
    prenom =models.CharField(max_length=45)
    sexe = models.CharField(max_length=8,choices=(('Male', 'Male'),('Femelle','Femelle'),))
    dateNaissance = models.DateField(null=True)
    lieuNaissance = models.CharField(max_length=100)
    lieuResidance = models.CharField(max_length=100)
    NumTel1 = models.IntegerField(null=True)
    NumTel2 = models.IntegerField(null=True)
    Assurance = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.nom}/{self.prenom}"


class Rendevous(models.Model):
    medecin_technicien = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    patient =  models.ForeignKey(Patient,blank=True,null=True,on_delete=models.CASCADE)
    dateRendevou = models.DateField(null=True)
    Status_Patient = models.TextField(max_length=1000)

    def __str__(self):
        return f"un Rendevous pour le Patient  {self.patient.nom} est Bien planifié"

class Consultation(models.Model):
    rendevous = models.ForeignKey(Rendevous,blank=True,null=True,on_delete=models.CASCADE)
    medecin = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    patient =  models.ForeignKey(Patient,blank=True,null=True,on_delete=models.CASCADE)
    dateConsultation = models.DateField(null=True)
    resultatConsultation = models.TextField(max_length=1000)

    def __str__(self):
        return f"la consultation de Patient  {self.patient.nom}/{self.patient.prenom}"

