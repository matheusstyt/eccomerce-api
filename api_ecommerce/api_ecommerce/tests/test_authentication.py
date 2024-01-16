from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teste123', password="12345678")
    def test_autenticacao_credenciais_incorretas(self):
        """Teste de verificação da autenticação do usuário"""
        user  =authenticate(username='teste123', password="12345678")
        self.assertTrue((user is not None) and user.is_authenticated)