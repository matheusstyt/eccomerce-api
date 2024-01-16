from django.db import models

class CategoryModel(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True, default="")
    slug = models.CharField(max_length=100, null=False)
    pai = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name
         