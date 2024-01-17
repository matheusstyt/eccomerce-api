from django.urls import include, path
from rest_framework import routers
from suppliers.views import ProductsSupplierView, SupplierViewSet

router = routers.DefaultRouter()

router.register('', SupplierViewSet, basename='Suppliers')
urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/products/', ProductsSupplierView.as_view(), name="supplier-products")
]
