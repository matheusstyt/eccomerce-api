from django.test import TestCase
from rest_framework.status import HTTP_200_OK

from django.contrib.auth.models import User
from rest_framework.test import APIClient

class TokenViewsTestCase(TestCase):
    
    TOKEN_URL = '/token/'
    REFRESH_URL = '/token/refresh'
    VERIFY_URL = '/token/verify'
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testetoken', password='12345678')
    
    def test_obter_token_jwt(self):
        '''Teste de obter token jwt por requisição POST'''
        response = self.client.post(self.TOKEN_URL, 
            {'username' : 'testetoken', 'password' : '12345678'}, format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        
    def test_renovar_token_jwt(self):
        '''Teste para renovar token jwt por requisição POST'''
        token_response = self.client.post(self.TOKEN_URL, 
            {'username' : 'testetoken', 'password' : '12345678'}, format='json')
        
        response = self.client.post(self.REFRESH_URL, 
            {'refresh' : token_response.data['refresh']}, format='json')
        
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertIn('access', response.data)
    
    def test_verificar_token_jwt(self):
        '''Teste para verificar token jwt por requisição POST'''
        token_response = self.client.post(self.TOKEN_URL, 
            {'username' : 'testetoken', 'password' : '12345678'}, format='json')
        
        response = self.client.post(self.VERIFY_URL, 
            {'token': token_response.data['access']}, format='json')
        
        self.assertEqual(response.status_code, HTTP_200_OK)
        