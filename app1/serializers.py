from rest_framework import serializers
from .models import SqlTable,HealthRecord


class SqlSerializer(serializers.ModelSerializer):
    class Meta:
        model=SqlTable
        fields='__all__'
        
class HelthSerializer(serializers.ModelSerializer):
    class Meta:
        model=HealthRecord
        fields='__all__'