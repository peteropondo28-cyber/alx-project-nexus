from rest_framework.test import APITestCase
from products.models import Category

class ProductAPITest(APITestCase):
    def test_product_list(self):
        Category.objects.create(name="Electronics")
        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, 200)
