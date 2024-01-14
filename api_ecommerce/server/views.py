import http
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
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
    
class AllProductsCategoryViewSet(ListAPIView):
    serializer_class=ProductSerializer
    def get_queryset(self):
        category = get_object_or_404(CategoryModel, pk=self.kwargs['pk'])
        print(category)
        print(self.kwargs['pk'])
        queryset = ProductModel.objects.filter(category=category)
        print(queryset)
        return queryset
    
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
    def create(self, request, *args, **kwargs):
        try:   
            response = super().create(request, *args, **kwargs)
            product_instance = self.get_object()
            price_history_instance = PriceHistoryModel.objects.create(
                product = product_instance,
                value = request.data.get('price')
            )
            print('chegou aqui 1')
            print(price_history_instance)
            return response
        except:
            return http.HTTPStatus.BAD_REQUEST
            
    def update(self, request, *args, **kwargs):
        print('oii')
        try:
            response = super().update(request, *args, **kwargs)
            product_instance = self.get_object()
            print('chegou aqui 2')
            if request.data.get('price'):
                price_history_instance = PriceHistoryModel.objects.create(
                    product = product_instance,
                    value = request.data.get('price')
                )
            return response
        except:
            return http.HTTPStatus.BAD_REQUEST
        
    def retrieve(self, request, *args, **kwargs):
        print('oi')
        try:
            response = super().retrieve(request, *args, **kwargs)
            product_instance = self.get_object()
            print('chegou aqui 3')
            print(request.data.get('price'))
            if request.data.get('price'):
                price_history_instance = PriceHistoryModel.objects.create(
                    product = product_instance,
                    value = request.data.get('price')
                )
                print(price_history_instance)
            return response
        except:
            return http.HTTPStatus.BAD_REQUEST
        
class AllReviewsProduct(ListAPIView):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        product = get_object_or_404(ProductModel, pk=self.kwargs['pk'])
        queryset = ReviewModel.objects.filter(product=product)
        return queryset
    
class RecommendedProducts(ListAPIView):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        product = get_object_or_404(ProductModel, pk=self.kwargs['pk'])
        queryset = ProductModel.objects.filter(categories=product.id)
        return queryset

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