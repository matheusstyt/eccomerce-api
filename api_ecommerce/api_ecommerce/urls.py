from django.urls import include, path
from server.views import *

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
  TokenVerifyView
)

from rest_framework import routers

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
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('doc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('token/', TokenObtainPairView.as_view(), name='get_new_token'),
    path('token/refresh', TokenRefreshView.as_view(), name='refresh_token'),
    path('token/verify', TokenVerifyView.as_view(), name='verify_token'),
]
