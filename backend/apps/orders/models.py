from django.db import models
from apps.tables.models import Table
from apps.dishes.models import Dishes
from django.core.exceptions import ValidationError


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    ]

    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, verbose_name="Стол", related_name="orders"
    )
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Общая стоимость", default=0.00
    )
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="Статус"
    )

    def clean(self):
        if self.pk:
            existing_order = Order.objects.filter(table=self.table, status__in=['pending', 'ready']).exclude(pk=self.pk)
        else:
            existing_order = Order.objects.filter(table=self.table, status__in=['pending', 'ready'])

        if existing_order.exists():
            raise ValidationError("This table is already reserved or has a pending order.")

        super().clean()

    def calculate_total_price(self):
        # Calculate total price based on related OrderDish objects
        total = 0
        for order_dish in self.order_dishes.all():
            total += order_dish.dish.price * order_dish.quantity
        return total

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.total_price = self.calculate_total_price()
        super().save(update_fields=['total_price'])

    def __str__(self):
        return f"Заказ {self.id} (Стол {self.table.number})"


class OrderDish(models.Model):
    order = models.ForeignKey(Order, related_name='order_dishes', on_delete=models.CASCADE)
    dish = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.dish.name} in Order {self.order.id}"
