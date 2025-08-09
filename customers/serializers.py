from rest_framework import serializers
from .models import Customer,DocumentType


class DocTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = '__all__'
class CustomerSerializer(serializers.ModelSerializer):
  doc_type = DocTypeSerializer(read_only=True)
  doc_type_id = serializers.PrimaryKeyRelatedField(
        queryset=DocumentType.objects.all(),
        source='doc_type',
        write_only=True
    )
  class Meta:
    model = Customer
    fields = '__all__'