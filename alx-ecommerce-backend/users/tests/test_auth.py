from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class AuthTest(APITestCase):
    def test_register(self):
        response = self.client.post("/api/auth/register/", {
            "username": "test",
            "email": "test@test.com",
            "password": "password123"
        })
        self.assertEqual(response.status_code, 201)
