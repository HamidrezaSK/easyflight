from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import AirlineSerializer
from .models import Airline

class AirlineList(generics.ListCreateAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer

class AirlineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer