from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FurnitureViewSet, ProviderViewSet

router = DefaultRouter()
router.register(r'furniture', FurnitureViewSet)
router.register(r'providers', ProviderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
