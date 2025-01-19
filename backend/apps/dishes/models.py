from django.db import models


# Create your models here.
class Dishes(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"Название: {self.name}, Цена: {self.price}$"
