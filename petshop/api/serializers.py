from rest_framework import serializers
from petshop.models import petshop

class petshopSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = petshop
        fields = "__all__"