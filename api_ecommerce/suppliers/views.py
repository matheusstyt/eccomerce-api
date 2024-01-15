from rest_framework.viewsets import ModelViewSet

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

from suppliers.models import SupplierModel
from suppliers.serializers import SupplierSerializer

class SupplierViewSet(ModelViewSet):
    filter_backends= [DjangoFilterBackend]
    filterset_fields = ['name', 'cnpj']
    queryset=SupplierModel.objects.all()
    serializer_class=SupplierSerializer
    authentication_classes= [BasicAuthentication]
    permission_classes= [IsAuthenticated]