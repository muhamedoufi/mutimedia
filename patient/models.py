from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    secretaire = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    nom = models.CharField(max_length=45)
    prenom =models.CharField(max_length=45)
    sexe = models.CharField(max_length=10)
    dateNaissance = models.DateField(null=True)
    lieuNaissance = models.CharField(max_length=100)
    lieuResidance = models.CharField(max_length=100)
    NumTel1 = models.IntegerField(null=True)
    NumTel2 = models.IntegerField(null=True)
    Assurance = models.CharField(max_length=45)

    def __str__(self):
        return f"le Patient  {self.nom}/{self.prenom} est bien Ajouteé"