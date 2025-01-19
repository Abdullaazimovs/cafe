from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.orders.api import OrderViewSet, OrderDishViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'order_dishes', OrderDishViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
