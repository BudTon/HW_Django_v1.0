from django.db import models


class Measurement(models.Model):
    temperature = models.FloatField(max_value=None, min_value=None)
    created_at = models.DateTimeField(auto_now=True)


class Sensor(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    measurements = models.ManyToManyField(Measurement, through='SensorDetail')


class SensorDetail(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensordetails')
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)




