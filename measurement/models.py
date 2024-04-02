from django.db import models


class Sensor (models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 50)
    objects = models.Manager()


class Measurement(models.Model):
    temperature = models.IntegerField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)