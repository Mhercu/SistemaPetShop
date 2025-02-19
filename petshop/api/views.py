from rest_framework.viewsets import ModelViewSet

from petshop.api.serializers import petshopSerializer

class petshopViewSet(ModelViewSet):
    serializer_class = petshopSerializer