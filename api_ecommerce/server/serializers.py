from rest_framework import serializers

from server.models import *

class PriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceHistoryModel
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = '__all__'
        
class AllReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = ['description']
        
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierModel
        fields = '__all__'
        