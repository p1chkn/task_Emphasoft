from django.test import TestCase
from rest_framework.test import APIClient
from .models import User


class ApiTest(TestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.user = User.objects.create(
            username='test_user',
            password='12345',
        )
        self.super_user = User.objects.create(
            username='superuser',
            password='12345',
            is_staff=True
        )

    def test_get(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)
        response = self.api_client.get(f'/api/v1/users/{self.user.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)

    def test_post(self):
        new_user = {
            'username': 'new_user',
            'password': '12345',
        }
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.post('/api/v1/users/')
        self.assertEqual(response.status_code, 403)
        self.api_client.force_authenticate(user=self.super_user)
        response = self.api_client.post('/api/v1/users/', new_user)
        self.assertEqual(response.status_code, 201)
        response = self.api_client.get('/api/v1/users/')
        self.assertContains(response, new_user['username'])

    def test_patch_self(self):
        new_data = {
            'username': 'new_test_user',
        }
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.patch(
            f'/api/v1/users/{self.user.id}/', new_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, new_data['username'])
