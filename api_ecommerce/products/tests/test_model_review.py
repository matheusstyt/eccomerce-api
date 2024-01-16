
import datetime
from unittest import TestCase
from categories.models import CategoryModel
from django.contrib.auth.models import User
from products.models import ProductModel, ReviewModel

class ReviewModelModelTestCase(TestCase):
    category2 = CategoryModel(
            id=2,
            name = "Categoria 2",
            slug = "categoria2"
        )
    user = User(
            username="admin",
            first_name="Admin",
            email="admin@admin.com",
            password="12345678"
        )
    product = ProductModel(
            category = category2,
            name= "Produto 2",
            internalCode= "0001",
            sku= "Dois",
            description= "Top 1 de vendas",
            price = 179,
            amount= 99,
        )
    def setUp(self):

        self.review = ReviewModel(
            title = "Titulo 1",
            product = self.product,
            user= self.user,
        )
    def test_verificando_atributos_do_reviews (self):
        """"Teste que verifica valores default de reviews"""
        self.assertEqual(self.review.user, self.user)
        self.assertEqual(self.review.product, self.product)
        self.assertEqual(self.review.rating, 3)
        self.assertEqual(self.review.title, "Titulo 1")
        self.assertEqual(self.review.description, "")
        
    