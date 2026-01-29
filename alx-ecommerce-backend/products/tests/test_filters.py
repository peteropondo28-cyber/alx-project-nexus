from rest_framework.test import APITestCase
from products.models import Category, Product

class ProductFilterTest(APITestCase):

    def setUp(self):
        category = Category.objects.create(name="Electronics")
        Product.objects.create(
            name="Phone",
            description="Smartphone",
            price=500,
            category=category
        )
        Product.objects.create(
            name="Laptop",
            description="Gaming Laptop",
            price=1500,
            category=category
        )

    def test_filter_by_category(self):
        response = self.client.get("/api/products/?category=Electronics")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 2)

    def test_sort_by_price_desc(self):
        response = self.client.get("/api/products/?ordering=-price")
        prices = [float(p["price"]) for p in response.data["results"]]
        self.assertEqual(prices, sorted(prices, reverse=True))
