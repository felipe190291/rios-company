from django_filters import rest_framework as filters
from .models import Customer
class CustomerModelFilter(filters.FilterSet):
  doc_type_name = filters.CharFilter(field_name='doc_type__code', lookup_expr='icontains')
  
  class Meta:
    model = Customer
    fields = ['doc_number','doc_type_name']