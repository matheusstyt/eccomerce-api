from django.test import TestCase
from suppliers.models import SupplierModel

class SupplierModelTestCase(TestCase):
    
    def setUp(self):
        self.supplier = SupplierModel(
            name = "Fornecedor 1",
            cnpj = "012345678912345"
        )
    def test_verificando_atributos_do_modelo_supplier(self):
        """"Teste que verifica valores default de supplier"""
        self.assertEqual(self.supplier.name, "Fornecedor 1")
        self.assertEqual(self.supplier.cnpj, "012345678912345")
        self.assertEqual(self.supplier.address, "")
        self.assertEqual(self.supplier.phone, "")
    
    