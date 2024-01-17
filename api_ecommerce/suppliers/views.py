from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from products.models import ProductModel
from products.serializers import ProductSerializer

from suppliers.models import SupplierModel
from suppliers.serializers import SupplierSerializer

class SupplierViewSet(ModelViewSet):
    filter_backends= [DjangoFilterBackend]
    filterset_fields = ['name', 'cnpj']
    queryset=SupplierModel.objects.all()
    serializer_class=SupplierSerializer
    authentication_classes= [BasicAuthentication]
    permission_classes= [IsAuthenticated]
    
class ProductsSupplierView(ListAPIView):
    serializer_class= ProductSerializer
    def get_queryset(self):
        supplier = get_object_or_404(SupplierModel, pk=self.kwargs['pk'])
        queryset = ProductModel.objects.filter(supplier=supplier)
        return queryset