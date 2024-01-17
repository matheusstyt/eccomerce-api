from rest_framework.test import APITestCase
from rest_framework.status import HTTP_401_UNAUTHORIZED

from django.urls import reverse

class ProductRequestTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Products-list')

    def test_requisicao_get_nao_autorizado(self):
        """Verifica se a requisição get passa sem logar no sistema"""
        response = self.client.get(self.list_url)
        self.assertNotEqual(response.status_code, HTTP_401_UNAUTHORIZED)
        
class ReviewRequestTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Reviews-list')

    def test_requisicao_get_nao_autorizado(self):
        """Verifica se a requisição get passa sem logar no sistema"""
        response = self.client.get(self.list_url)
        self.assertNotEqual(response.status_code, HTTP_401_UNAUTHORIZED)
        
class PriceHistoryRequestTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('PriceHistories-list')

    def test_requisicao_get_nao_autorizado(self):
        """Verifica requisição get que não for autenticado"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)
        