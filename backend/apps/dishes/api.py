from rest_framework import viewsets

from apps.dishes import serializers, models


class DishViewSet(viewsets.ModelViewSet):
    queryset = models.Dishes.objects.all()
    serializer_class = serializers.DishesSerializer
