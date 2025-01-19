from django.urls import path, include
from apps.dishes import api
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"", api.DishViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

