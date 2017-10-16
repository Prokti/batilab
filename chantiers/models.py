from django.db import models
from profil.models import Profil
from django.contrib.auth.models import User

# Create your models here.

class Chantier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField(null=False)
    ccmi_doc = models.FileField(upload_to='')
    appel_1_doc = models.FileField(upload_to='')
    appel_2_doc = models.FileField(upload_to='')
    appel_3_doc = models.FileField(upload_to='')
    appel_4_doc = models.FileField(upload_to='')
    appel_5_doc = models.FileField(upload_to='')
    reception_doc = models.FileField(upload_to='')
    plans_os_doc = models.FileField(upload_to='')


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

