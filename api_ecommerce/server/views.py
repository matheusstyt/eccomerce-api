from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from server.models import *
from server.serializers import *

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

class CategoryViewSet(viewsets.ModelViewSet):
    filter_backends= [DjangoFilterBackend]
    filterset_fields = ['name', 'slug']
    queryset=CategoryModel.objects.all()
    serializer_class=CategorySerializer
    authentication_classes= [BasicAuthentication]
    permission_classes= [IsAuthenticated]
    

class PriceHistoryViewSet(viewsets.ModelViewSet):
    queryset=PriceHistoryModel.objects.all()
    serializer_class=PriceHistorySerializer
    authentication_classes= [BasicAuthentication]
    permission_classes= [IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    filter_backends= [DjangoFilterBackend]
    filterset_fields = ['name']
    queryset=ProductModel.objects.all()
    serializer_class=ProductSerializer    
    authentication_classes= [BasicAuthentication]
    permission_classes= [IsAuthenticated]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset=ReviewModel.objects.all()
    serializer_class=ReviewSerializer
    authentication_classes= [BasicAuthentication]
    permission_classes= [IsAuthenticated]

class SupplierViewSet(viewsets.ModelViewSet):
    filter_backends= [DjangoFilterBackend]
    filterset_fields = ['name', 'cnpj']
    queryset=SupplierModel.objects.all()
    serializer_class=SupplierSerializer
    authentication_classes= [BasicAuthentication]
    permission_classes= [IsAuthenticated]