from rest_framework import viewsets

from server.models import *
from server.serializers import *

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=CategoryModel.objects.all()
    serializer_class=CategorySerializer
    

class PriceHistoryViewSet(viewsets.ModelViewSet):
    queryset=PriceHistoryModel.objects.all()
    serializer_class=PriceHistorySerializer
    

class ProductViewSet(viewsets.ModelViewSet):
    queryset=ProductModel.objects.all()
    serializer_class=ProductSerializer    


class ReviewViewSet(viewsets.ModelViewSet):
    queryset=ReviewModel.objects.all()
    serializer_class=ReviewSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset=SupplierModel.objects.all()
    serializer_class=SupplierSerializer