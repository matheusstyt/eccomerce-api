from graphene_django import DjangoObjectType

from products.models import *

class ProductType(DjangoObjectType):
    class Meta:
        model = ProductModel
        fields = "__all__"

class ReviewType(DjangoObjectType):
    class Meta:
        model = ReviewModel
        fields = "__all__"

class PriceHistoryType(DjangoObjectType):
    class Meta:
        model = PriceHistoryModel
        fields = "__all__"
