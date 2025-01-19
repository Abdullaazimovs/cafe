from rest_framework import viewsets

from apps.orders.models import Order, OrderDish
from apps.orders.serializers import OrderCreateSerializer, OrderDishSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer


class OrderDishViewSet(viewsets.ModelViewSet):
    queryset = OrderDish.objects.all()
    serializer_class = OrderDishSerializer
