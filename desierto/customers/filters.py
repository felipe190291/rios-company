from django_filters import rest_framework as filters
from .models import Customer
class CustomerModelFilter(filters.FilterSet):
  # doc_number = filters.CharFilter(lookup_expr='icontains')
  class Meta:
    model = Customer
    fields = ['doc_number']