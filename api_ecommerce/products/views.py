import http
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from products.models import *
from products.serializers import *

from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import BasicAuthentication

class IsGetOrAuthenticated(BasePermission):
    def has_permission(self, request, view):
        # Permite get para todos
        return request.method == 'GET' or request.user and request.user.is_authenticated

class PriceHistoryViewSet(ModelViewSet):
    queryset=PriceHistoryModel.objects.all()
    serializer_class=PriceHistorySerializer
    authentication_classes= [BasicAuthentication]
    permission_classes= [IsAuthenticated]

class ProductViewSet(ModelViewSet):
    filter_backends= [DjangoFilterBackend]
    filterset_fields = ['name']
    queryset=ProductModel.objects.all()
    serializer_class=ProductSerializer    
    authentication_classes= [BasicAuthentication]
    permission_classes= [IsGetOrAuthenticated]
    
    def create(self, request, *args, **kwargs):
        try:   
            response = super().create(request, *args, **kwargs)
            product_instance = self.get_object()
            price_history_instance = PriceHistoryModel.objects.create(
                product = product_instance,
                value = request.data.get('price')
            )
            return response
        except:
            return http.HTTPStatus.BAD_REQUEST
            
    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            product_instance = self.get_object()
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
    serializer_class = ProductSerializer
    def get_queryset(self):
        product = get_object_or_404(ProductModel, pk=self.kwargs['pk'])
        queryset = ProductModel.objects.filter(category=product.category).exclude(pk=product.pk)
        return queryset

class ReviewViewSet(ModelViewSet):
    queryset=ReviewModel.objects.all()
    serializer_class=ReviewSerializer
    authentication_classes= [BasicAuthentication]
    permission_classes= [IsGetOrAuthenticated]