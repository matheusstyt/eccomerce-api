from django.urls import include, path

from drf_spectacular.views import *

from rest_framework_simplejwt.views import *

from rest_framework import routers

router = routers.DefaultRouter()

from products.urls import urlpatterns as products_urls
from categories.urls import urlpatterns as categories_urls
from suppliers.urls import urlpatterns as suppliers_urls

from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('products/', include(products_urls)),
    path('categories/', include(categories_urls)),
    path('suppliers/', include(suppliers_urls)),
    path('doc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('token/', TokenObtainPairView.as_view(), name='get_new_token'),
    path('token/refresh', TokenRefreshView.as_view(), name='refresh_token'),
    path('token/verify', TokenVerifyView.as_view(), name='verify_token'),
]
