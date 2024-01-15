from django.db import models

from products.models import ProductModel

class SupplierModel(models.Model):
    name = models.CharField(max_length=255, null=True)
    cnpj = models.CharField(max_length=14, unique=True)
    address = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=20)
    products = models.ManyToManyField(ProductModel, related_name='suppliers', blank=True)
    def __str__(self) -> str:
        return self.name