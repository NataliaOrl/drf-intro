from rest_framework import generics
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementCreateSerializer
from .models import Sensor, Measurement


class SensorCreateAPIView(generics.CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreateView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer

