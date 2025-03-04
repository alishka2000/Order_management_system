from django.test import TestCase
from .models import Order

class OrderTestCase(TestCase):
    def test_create_order(self):
        order = Order.objects.create(table_number=1, items=[{"name": "Пицца", "price": 500}])
        self.assertEqual(order.total_price, 500)