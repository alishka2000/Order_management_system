from django.test import TestCase
from .models import Order
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
django.setup()

class OrderTestCase(TestCase):
    def test_create_order(self):
        order = Order.objects.create(table_number=1, items=[{"name": "Пицца", "price": 500}])

        # Пересчитаем сумму
        order.calculate_total_price()  # если у тебя есть такой метод

        self.assertEqual(order.total_price, 500)


# Запуск теста
if __name__ == "__main__":
    OrderTestCase()