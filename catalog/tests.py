from django.test import TestCase
from models import Product,TV


class Test(TestCase):
    def setUp(self):
        Product.objects.create(id=5,product_category_id=1,product_presence=True)
        Product.objects.create(id=6,product_category_id=1,product_presence=False)

    def test_product_get(self):
        first = Product.objects.get(id=5)
        second = Product.objects.get(id=6)
        self.assertEqual(first.get_absolute_url(),'/product/5/')
        self.assertEqual(second.get_absolute_url(),'/product/6/')

    def test_product_presence(self):
        first = Product.objects.get(id=5)
        second = Product.objects.get(id=6)
        self.assertEqual(first.is_available(),'Exists')
        self.assertEqual(second.is_available(),'Not exist')