from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from categories.models import CategoryModel
from categories.serializers import CategorySerializer
from products.models import ProductModel
from products.serializers import ProductSerializer

class CategoryViewSet(ModelViewSet):
    filter_backends= [DjangoFilterBackend]
    filterset_fields = ['name', 'slug']
    queryset=CategoryModel.objects.all()
    serializer_class=CategorySerializer
    authentication_classes= [BasicAuthentication]
    permission_classes= [IsAuthenticated]
    
class AllProductsCategoryViewSet(ListAPIView):
    serializer_class=ProductSerializer
    def get_queryset(self):
        category = get_object_or_404(CategoryModel, pk=self.kwargs['pk'])
        queryset = ProductModel.objects.filter(category=category)
        return queryset