from django.test import TestCase

from categories.models import CategoryModel

class CategoryModelTestCase(TestCase):
    
    def setUp(self):
        self.category = CategoryModel(
            name = "Categoria 1",
            slug = "categoria1"
        )
    def test_verificando_atributos_do_modelo_category(self):
        """"Teste que verifica valores dafault de category"""
        self.assertEqual(self.category.name, "Categoria 1")
        self.assertEqual(self.category.description, "")
        self.assertEqual(self.category.slug, "categoria1")
    
    