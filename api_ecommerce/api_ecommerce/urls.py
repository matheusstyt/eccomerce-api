from django.urls import include, path
from rest_framework import routers

from server.views import CategoryViewSet, PriceHistoryViewSet, ProductViewSet, ReviewViewSet, SupplierViewSet

router = routers.DefaultRouter()

router.register('products', ProductViewSet, basename='Products')
router.register('categories', CategoryViewSet, basename='Categories')
router.register('priceHistory', PriceHistoryViewSet, basename='PriceHistories')
router.register('reviews', ReviewViewSet, basename='Reviews')
router.register('suppliers', SupplierViewSet, basename='Suppliers')

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
