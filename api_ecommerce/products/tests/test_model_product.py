from django.test import TestCase

from suppliers.models import SupplierModel

from categories.models import CategoryModel

from products.models import ProductModel

class ProductsModelTestCase(TestCase):
    category1 = CategoryModel(
        name = "Categoria 1",
        slug = "categoria1"
    )
    def setUp(self):
        self.product = ProductModel(
            name = "Produto 1",
            category = self.category1
        )
    def test_verificando_atributos_do_modelo_product(self):
        """"Teste que verifica valores default de products"""
        self.assertEqual(self.product.name, "Produto 1")
        self.assertEqual(self.product.category, self.category1)
        self.assertEqual(self.product.internalCode, "")
        self.assertEqual(self.product.sku, "")
        self.assertEqual(self.product.description, "")
        self.assertEqual(self.product.price, 0)
        self.assertEqual(self.product.amount, 0)
    