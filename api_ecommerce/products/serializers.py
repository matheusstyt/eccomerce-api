from rest_framework import serializers

from products.models import PriceHistoryModel, ProductModel, ReviewModel

class ProductSerializer(serializers.ModelSerializer):
    total_rating = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        fields = '__all__'

    def get_total_rating(self, obj):
        reviews = ReviewModel.objects.filter(product=obj)
        total_rating = sum(review.rating for review in reviews)
        return total_rating if reviews else 0

    def get_average_rating(self, obj):
        reviews = ReviewModel.objects.filter(product=obj)
        count_reviews = reviews.count()
        total_rating = sum(review.rating for review in reviews)
        average_rating = total_rating / count_reviews if count_reviews else 0
        return round(average_rating, 2)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = '__all__'

class PriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceHistoryModel
        fields = '__all__'