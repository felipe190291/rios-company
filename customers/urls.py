from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, DocTypeViewSet, ReportView

router = DefaultRouter()
router.register(r"customer", CustomerViewSet)
router.register(r"document_type", DocTypeViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("report/", ReportView.as_view(({"get": "list"})), name="report"),
]
