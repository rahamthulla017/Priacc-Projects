from rest_framework import viewsets
from django.shortcuts import render
from .models import Service, Product, ContactMessage
from .serializers import ServiceSerializer, ProductSerializer, ContactMessageSerializer

# API ViewSets
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

# Template Views
def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def products(request):
    return render(request, 'products.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
