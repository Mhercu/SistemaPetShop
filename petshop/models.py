from django.db import models

class Usuario(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    autenticado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Administrador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    cargo = models.CharField(max_length=255, default='Administrador')

    def __str__(self):
        return f'Administrador: {self.usuario.nome}'

class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'Cliente: {self.usuario.nome}'

class Veterinario(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    crmv = models.CharField(max_length=255)  # Registro profissional do veterinário

    def __str__(self):
        return f'Veterinário: {self.usuario.nome}'

class Produto(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    nome = models.CharField(max_length=255)
    preco = models.FloatField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class DadosMedicos(models.Model):
    historico = models.TextField(blank=True, null=True)
    vacinas = models.TextField(blank=True, null=True)
    alergias = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Dados Médicos: {self.id}'

class Pet(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    nome = models.CharField(max_length=255)
    especie = models.CharField(max_length=255)
    raca = models.CharField(max_length=255)
    idade = models.IntegerField()
    peso = models.FloatField()
    observacoes = models.TextField(blank=True, null=True)
    dados_medicos = models.OneToOneField(DadosMedicos, on_delete=models.SET_NULL, null=True, blank=True)
    dono = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    servico = models.CharField(max_length=255)
    profissional = models.ForeignKey(Veterinario, on_delete=models.SET_NULL, null=True, blank=True)
    data_hora = models.DateTimeField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True, blank=True)
    confirmado = models.BooleanField(default=False)

    def __str__(self):
        return f'Agendamento: {self.servico} - {self.data_hora}'
