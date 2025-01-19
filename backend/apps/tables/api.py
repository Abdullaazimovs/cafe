from rest_framework import viewsets

from apps.tables.models import Table
from apps.tables.serializers import TablesSerializer


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TablesSerializer
