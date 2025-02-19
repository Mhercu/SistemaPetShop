from django.db import models

# Create your models here.


class petshop(models.Model):
    nome = models.CharField(max_length=50)
    peso = models.IntegerField(max_length=50)
    especie = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)
    idade = models.IntegerField(max_length=50)
 
