from django.urls import include, path
from rest_framework import routers

from django.contrib import admin

from api_ecommerce.server.views import CategoryViewSet, PriceHistoryViewSet, ProductViewSet, ReviewViewSet, SupplierViewSet

router = routers.DefaultRouter()

router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('priceHistory', PriceHistoryViewSet)
router.register('products', ProductViewSet)
router.register('reviews', ReviewViewSet)
router.register('suppliers', SupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
