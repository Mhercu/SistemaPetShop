from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from petshop.models import Usuario, Administrador, Cliente, Veterinario, Produto, DadosMedicos, Pet, Agendamento
from petshop.api.serializers import (
    UsuarioSerializer, AdministradorSerializer, ClienteSerializer, VeterinarioSerializer,
    ProdutoSerializer, DadosMedicosSerializer, PetSerializer, AgendamentoSerializer
)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class VeterinarioViewSet(viewsets.ModelViewSet):
    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class DadosMedicosViewSet(viewsets.ModelViewSet):
    queryset = DadosMedicos.objects.all()
    serializer_class = DadosMedicosSerializer

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

    @action(detail=True, methods=['post'])
    def processar_agendamento(self, request, pk=None):
        agendamento = self.get_object()
        if not agendamento:
            return Response({'erro': 'Agendamento não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        if agendamento.profissional and agendamento.dataHora:
            agendamento.confirmado = True
            agendamento.save()
            return Response({'mensagem': 'Agendamento confirmado'}, status=status.HTTP_200_OK)
        
        return Response({'mensagem': 'Horário indisponível, sugerir outro horário'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def processar_consulta(self, request, pk=None):
        agendamento = self.get_object()
        if not agendamento:
            return Response({'erro': 'Agendamento não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        pet = agendamento.pet
        if not pet:
            return Response({'erro': 'Pet não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        if 'tratamento_necessario' in request.data and request.data['tratamento_necessario']:
            pet.dados_medicos.historico += "\nTratamento realizado."
            pet.dados_medicos.save()
        
        return Response({'mensagem': 'Consulta finalizada, recomendações enviadas ao cliente'}, status=status.HTTP_200_OK)