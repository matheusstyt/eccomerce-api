from django.db import models

class SupplierModel(models.Model):
    name = models.CharField(max_length=255, null=False, default="")
    cnpj = models.CharField(max_length=14, unique=True, null=False)
    address = models.CharField(max_length=255, null=True, blank=True, default="")
    phone = models.CharField(max_length=20,blank=True, default="")
    
    def __str__(self) -> str:
        return self.name
    