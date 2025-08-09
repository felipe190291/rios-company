from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer
from .filters import CustomerModelFilter
from django_filters.rest_framework import DjangoFilterBackend
class CustomerViewSet(viewsets.ModelViewSet):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer
  filterset_class =CustomerModelFilter
  filter_backends = [DjangoFilterBackend]
