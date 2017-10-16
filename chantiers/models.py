from django.db import models
from profil.models import Profil
from django.contrib.auth.models import User
import os, random

# Create your models here.

def renommage(instance, nom):
    aleatoire = random.random()
    nom_fichier = os.path.splitext(nom)[0]
    return "{}--{}--{}".format(instance.id, nom_fichier, aleatoire)

class Chantier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField(null=False)
    ccmi_doc = models.FileField(upload_to=renommage, verbose_name="CCMI")
    appel_1_doc = models.FileField(upload_to=renommage)
    appel_2_doc = models.FileField(upload_to=renommage)
    appel_3_doc = models.FileField(upload_to=renommage)
    appel_4_doc = models.FileField(upload_to=renommage)
    appel_5_doc = models.FileField(upload_to=renommage)
    reception_doc = models.FileField(upload_to=renommage)
    plans_os_doc = models.FileField(upload_to=renommage)


    #profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Marche(models.Model):

    name = models.CharField(max_length=100)
    chantier = models.ForeignKey(Chantier, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    marche_doc = models.FileField(upload_to='')
    devis_doc = models.FileField(upload_to='')
     


    def __str__(self):
        return self.name



