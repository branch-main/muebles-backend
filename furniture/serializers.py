from rest_framework import serializers
from .models import Furniture, Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['id', 'name', 'city', 'phone', 'email']


class FurnitureSerializer(serializers.ModelSerializer):
    provider_name = serializers.CharField(source='provider.name', read_only=True)
    
    class Meta:
        model = Furniture
        fields = ['id', 'provider', 'provider_name', 'name', 'material', 'price', 'stock', 'image']
