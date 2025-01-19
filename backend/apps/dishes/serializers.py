from rest_framework import serializers
from apps.dishes import models


class DishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dishes
        fields = "__all__"
