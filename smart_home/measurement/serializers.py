from rest_framework import serializers
from .models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class MeasurementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']


class MeasurementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementListSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
