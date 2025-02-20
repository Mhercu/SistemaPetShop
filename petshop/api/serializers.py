from rest_framework import serializers
from petshop.models import (
    Usuario, Produto, Pet, Agendamento, DadosMedicos, 
    Administrador, Cliente, Veterinario
)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class VeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class DadosMedicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosMedicos
        fields = '__all__'

class PetSerializer(serializers.ModelSerializer):
    dados_medicos = DadosMedicosSerializer(read_only=True)

    class Meta:
        model = Pet
        fields = '__all__'

class AgendamentoSerializer(serializers.ModelSerializer):
    pet = PetSerializer(read_only=True)
    pet_id = serializers.PrimaryKeyRelatedField(
        queryset=Pet.objects.all(), source='pet', write_only=True
    )

    class Meta:
        model = Agendamento
        fields = '__all__'
