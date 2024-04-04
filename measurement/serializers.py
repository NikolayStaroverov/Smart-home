from rest_framework import serializers
from .models import Measurement, Sensor


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'sensor','created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
     class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']