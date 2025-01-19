from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.tables.api import TableViewSet

router = DefaultRouter()
router.register(r'', TableViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
