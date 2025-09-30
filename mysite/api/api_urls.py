# api/api_urls.py
from django.urls import path, include
from rest_framework import routers
from .views import ServiceViewSet, ProductViewSet, ContactMessageViewSet

router = routers.DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'products', ProductViewSet)
router.register(r'contacts', ContactMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
