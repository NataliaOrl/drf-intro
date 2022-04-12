from django.contrib import admin
from .models import Sensor, Measurement


class MeasurementInline(admin.TabularInline):
    model = Measurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    inlines = [
        MeasurementInline
    ]


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    pass