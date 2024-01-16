from django.contrib.auth.models import User
from django.db import models
from suppliers.models import SupplierModel

from categories.models import CategoryModel
from django.core.validators import MinValueValidator, MaxValueValidator

class ProductModel(models.Model):
    name = models.CharField(max_length=255, null=False)
    internalCode = models.CharField(max_length=255, null=True, blank=True, default="")
    sku = models.CharField(max_length=255, null=True, blank=True, default="")
    description = models.TextField(null=True, blank=True, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    amount = models.IntegerField(blank=True, default=0)
    supplier = models.ForeignKey(SupplierModel, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
class PriceHistoryModel(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.value)

class ReviewModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    rating = models.IntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True, default="")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.description