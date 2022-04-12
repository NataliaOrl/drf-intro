from django.urls import path
from .views import SensorListCreateAPIView, SensorRetrieveUpdateAPIView, MeasurementCreateView
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('sensors/', SensorListCreateAPIView.as_view()),
    path('sensors/<pk>/', SensorRetrieveUpdateAPIView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
]
