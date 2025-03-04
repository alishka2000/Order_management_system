from django.db import models
from django.db.models import Sum


class Order(models.Model):
    STATUS_CHOICES = [
        ("в ожидании", "В ожидании"),
        ("готово", "Готово"),
        ("оплачено", "Оплачено"),
    ]

    table_number = models.IntegerField(verbose_name="Номер стола")
    items = models.JSONField(
        "Список блюд с ценами",
        help_text='Введите данные в формате: [{"name": "Блюдо", "price": 100}, {"name": "Блюдо2", "price": 200}]'
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Общая стоимость")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="в ожидании", verbose_name="Статус")

    def save(self, *args, **kwargs):
        self.total_price = sum(item["price"] for item in self.items)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Заказ {self.id} - Стол {self.table_number}"

    @classmethod
    def get_revenue(cls):
        return cls.objects.filter(status="paid").aggregate(total_revenue=Sum("total_price"))["total_revenue"] or 0