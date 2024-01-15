from django.urls import include, path
from rest_framework import routers
from suppliers.views import SupplierViewSet

router = routers.DefaultRouter()

router.register('', SupplierViewSet, basename='Suppliers')
urlpatterns = [
    path('', include(router.urls)),
]
