from django.db import models
from django.contrib.auth.models import User

    
class CategoryModel(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField()
    slug = models.CharField(max_length=100, null=True)
    pai = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name
         
class ProductModel(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=2, decimal_places=2, default=0, null=True)
    amount = models.IntegerField()
    
    categories = models.ForeignKey(CategoryModel, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name 
    
class PriceHistoryModel(models.Model):
    value = models.DecimalField(max_digits=2, decimal_places=2)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.value)

class ReviewModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.description
    
class SupplierModel(models.Model):
    name = models.CharField(max_length=255, null=True)
    cnpj = models.CharField(max_length=14, unique=True)
    address = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=20)
    products = models.ManyToManyField(ProductModel, related_name='fornecedores', blank=True)
    def __str__(self) -> str:
        return self.name