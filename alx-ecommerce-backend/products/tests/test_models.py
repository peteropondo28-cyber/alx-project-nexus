from django.test import TestCase
from products.models import Category, Product

class ProductModelTest(TestCase):
    def test_category_unique(self):
        Category.objects.create(name="Books")
        with self.assertRaises(Exception):
            Category.objects.create(name="Books")
