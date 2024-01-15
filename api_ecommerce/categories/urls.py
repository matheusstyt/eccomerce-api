from django.urls import include, path
from rest_framework import routers
from categories.views import AllProductsCategoryViewSet, CategoryViewSet

router = routers.DefaultRouter()

router.register('', CategoryViewSet, basename='Categories')

urlpatterns = [
    
    path('', include(router.urls)),
    path('<int:pk>/products/', AllProductsCategoryViewSet.as_view()),

]
