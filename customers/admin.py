from django.contrib import admin

# Register your models here.
from .models import DocumentType,Customer,Purchase

admin.site.register(DocumentType)
admin.site.register(Customer)
admin.site.register(Purchase)