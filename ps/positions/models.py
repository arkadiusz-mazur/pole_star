from django.db import models

class Ship(models.Model):

    imo = models.IntegerField()
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'ships'

class Position(models.Model):
    imo = models.IntegerField()
    signal_time = models.DateTimeField()
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return self.imo

    class Meta:
        verbose_name_plural = 'positions'
