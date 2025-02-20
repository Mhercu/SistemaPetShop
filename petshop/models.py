from django.db import models

class Usuario(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    autenticado = models.BooleanField(default=False)

class Produto(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    nome = models.CharField(max_length=255)
    preco = models.FloatField()
    descricao = models.TextField()

class Pet(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    nome = models.CharField(max_length=255)
    especie = models.CharField(max_length=255)
    raca = models.CharField(max_length=255)
    idade = models.IntegerField()
    peso = models.FloatField()
    observacoes = models.TextField()

class Agendamento(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    servico = models.CharField(max_length=255)
    profissional = models.CharField(max_length=255)
    data_hora = models.DateTimeField()

