from django.db import models


class Table(models.Model):
    number: int = models.IntegerField(unique=True, verbose_name="Номер стола")
    seats: int = models.IntegerField(verbose_name="Количество мест", default=4)

    def __str__(self) -> str:
        return f"Стол {self.number} ({self.seats} мест)"
