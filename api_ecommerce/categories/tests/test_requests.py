from rest_framework.test import APITestCase
from rest_framework.status import HTTP_401_UNAUTHORIZED

from django.urls import reverse
class CategoryRequestTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Categories-list')

    def test_requisicao_get_nao_autorizado(self):
        """Verifica se a requisição get passa sem logar no sistema"""
        response = self.client.get(self.list_url)
        self.assertNotEqual(response.status_code, HTTP_401_UNAUTHORIZED)
        