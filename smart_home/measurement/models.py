from django.db import models


class Sensor(models.Model):
    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
    name = models.CharField(max_length=255, verbose_name='название')
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name='описание')

    def __str__(self):
        return self.name


class Measurement(models.Model):
    class Meta:
        verbose_name = 'Показания датчика'
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', verbose_name='датчик')
    temperature = models.FloatField(verbose_name='температура')
    created_at = models.DateTimeField(auto_now=True, verbose_name='время измерения')

    def __str__(self):
        return f'{self.created_at}: {self.sensor.name} {self.temperature}'
