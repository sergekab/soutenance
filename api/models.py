from django.db import models


class Programme(models.Model):
    description = models.CharField(max_length=500)
    detail = models.CharField(max_length=200)

class Utilisateur(models.Model):
    nom = models.CharField(max_length=200)
    email = models.CharField(max_length=200) 

class Evenement(models.Model):
    nom = models.CharField(max_length=200)
    date = models.DateField()
    heure = models.TimeField()
    lieu = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    organisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)





