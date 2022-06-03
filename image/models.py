from io import BytesIO
from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient
from PIL import Image as im
import matplotlib.pyplot as plt
import numpy as np
# Create your models here.

class Image(models.Model):
    img = models.ImageField(upload_to='image/images/',blank=True, null=True)
    type = models.CharField(max_length=30)
    technicien = models.ForeignKey(User,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    description = models.TextField()


    def __str__(self):
        return f"l'image du Patient  {self.patient} est bien Ajouteé"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        image = im.open(self.img.path)
        if image.width > 300 or image.height > 300:
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.img.path)
   
