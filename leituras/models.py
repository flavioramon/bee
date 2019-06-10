"""Modelos da aplicação leituras."""

from django.db import models
from model_utils.models import TimeStampedModel


class Leitura(TimeStampedModel):
    """Uma leitura obtida a partir do "mini-pc" via csv."""

    reading_time_local = models.DateTimeField()
    bee_id = models.CharField(max_length=24)
    tid = models.CharField(max_length=24)
    antenna = models.IntegerField()
    pc_id = models.CharField(max_length=100)
    ambient_temperature = models.FloatField()
    pwr_amp_temperature = models.FloatField()
    reader_status = models.IntegerField()
    ms_counter = models.FloatField()
    nb_rssi = models.CharField(max_length=15)
    wb_rssi = models.CharField(max_length=23)
    gain = models.FloatField()
    rssi = models.FloatField()

    class Meta:
        """Meta opções do modelo."""

        ordering = ['id']

    def __str__(self):
        """toString."""
        return f'[{self.reading_time_local}][{self.bee_id}]'
