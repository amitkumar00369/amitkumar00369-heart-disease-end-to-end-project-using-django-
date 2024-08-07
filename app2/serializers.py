from rest_framework import serializers

from .models import MongoTable

class MongoSerializer(serializers.Serializer):
    class Meta:
        model=MongoTable
        fields='__all__'