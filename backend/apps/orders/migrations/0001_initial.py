# Generated by Django 5.1.5 on 2025-01-15 17:06

import django
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("dishes", "0001_initial"),
        ("tables", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "total_price",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=10,
                        verbose_name="Общая стоимость",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "В ожидании"),
                            ("ready", "Готово"),
                            ("paid", "Оплачено"),
                        ],
                        default="pending",
                        max_length=10,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "table",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to="tables.table",
                        verbose_name="Стол",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderDish",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "dish",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="dishes.dishes"
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_dishes",
                        to="orders.order",
                    ),
                ),
            ],
        ),
    ]
