from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Car
from .serializers import CarSerializer
# Create your views here.


class CRUD_CarView(ModelViewSet):
    """CRUD car view"""
    # viewset is the best choice for standart CRUD
    queryset = Car.objects.all()
    serializer_class = CarSerializer
