from rest_framework import viewsets
from .models import Furniture, Provider
from .serializers import FurnitureSerializer, ProviderSerializer


class FurnitureViewSet(viewsets.ModelViewSet):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
