from django.urls import include, path
from rest_framework import routers
from products.views import AllReviewsProduct, PriceHistoryViewSet, ProductViewSet, RecommendedProducts, ReviewViewSet

router = routers.DefaultRouter()

router.register('', ProductViewSet, basename='Products')
router.register('priceHistory', PriceHistoryViewSet, basename='PriceHistories')
router.register('reviews', ReviewViewSet, basename='Reviews')
urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/reviews/', AllReviewsProduct.as_view(), name='product-reviews'),
    path('<int:pk>/recomended/', RecommendedProducts.as_view(), name='product-recommended'),
]
