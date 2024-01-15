from rest_framework.serializers import ModelSerializer

from products.models import PriceHistoryModel, ProductModel, ReviewModel

class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'
        
class ReviewSerializer(ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = '__all__'

class PriceHistorySerializer(ModelSerializer):
    class Meta:
        model = PriceHistoryModel
        fields = '__all__'