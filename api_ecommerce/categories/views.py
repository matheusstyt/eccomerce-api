from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from categories.serializers import CategorySerializer
from products.serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from django.shortcuts import get_object_or_404
from categories.models import CategoryModel
from products.models import ProductModel

class IsGetOrAuthenticated(BasePermission):
    def has_permission(self, request, view):
        # Permite get para todos
        return request.method == 'GET' or request.user and request.user.is_authenticated

class CategoryViewSet(ModelViewSet):
    filter_backends= [DjangoFilterBackend]
    filterset_fields = ['name', 'slug']
    queryset=CategoryModel.objects.all()
    serializer_class=CategorySerializer
    authentication_classes= [BasicAuthentication]
    permission_classes= [IsGetOrAuthenticated]
    
class AllProductsCategoryViewSet(ListAPIView):
    permission_classes= [IsGetOrAuthenticated]
    serializer_class=ProductSerializer
    
    def get_queryset(self):
        category = get_object_or_404(CategoryModel, pk=self.kwargs['pk'])
        queryset = ProductModel.objects.filter(category=category)
        return queryset