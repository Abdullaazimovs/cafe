from rest_framework import serializers
from apps.tables import models


class TablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Table
        fields = ["number", "seats"]
