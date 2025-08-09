from datetime import datetime, timedelta

import pandas as pd
from django.db.models import Sum
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .filters import CustomerModelFilter
from .models import Customer, DocumentType, Purchase
from .serializers import CustomerSerializer, DocTypeSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_class = CustomerModelFilter
    filter_backends = [DjangoFilterBackend]


class DocTypeViewSet(viewsets.ModelViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocTypeSerializer


class ReportView(viewsets.ViewSet):
    def list(self, request):
        today = datetime.now()
        one_month_ago = today - timedelta(days=30)

        purchases = (
            Purchase.objects.filter(date__gte=one_month_ago, date__lte=today)
            .values(
                "client__id",
                "client__first_name",
                "client__last_name",
                "client__email",
                "client__phone",
                "client__doc_number",
            )
            .annotate(total_amount=Sum("amount"))
        )
        df = pd.DataFrame(list(purchases))
        df.rename(
            columns={
                "client__id": "ID",
                "client__first_name": "Nombre",
                "client__last_name": "Apellido",
                "client__email": "Email",
                "client__doc_number": "Documento",
                "client__phone": "Telefono",
                "total_amount": "Total Compras",
            },
            inplace=True,
        )
        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response["Content-Disposition"] = 'attachment; filename="reporte_compras.xlsx"'
        with pd.ExcelWriter(response, engine="openpyxl") as writer:
            df.to_excel(writer, index=False)
        return response
