from django.contrib import admin
from django.forms import Textarea
from django.db import models
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "table_number", "total_price", "status")
    list_filter = ("status",)
    search_fields = ("table_number",)
    formfield_overrides = {
        models.JSONField: {"widget": Textarea(attrs={
            "rows": 5, "cols": 60,
            "placeholder": '[{"name": "Борщ", "price": 500}, {"name": "Чай", "price": 200}]'
        })},
    }
    readonly_fields = ("total_price",)
    exclude = ("total_price",)
admin.site.register(Order, OrderAdmin)