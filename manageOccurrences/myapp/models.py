from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

STATE_CHOICES = (('POR VALIDAR', 'POR VALIDAR'), ('VALIDADO', 'VALIDADO'), ('RESOLVIDO', 'RESOLVIDO'))
CATEGORY_CHOICES = (('CONSTRUCTION', 'CONSTRUCTION'), ('SPECIAL_EVENT', 'SPECIAL_EVENT'), ('INCIDENT', 'INCIDENT'),
                    ('WEATHER_CONDITION', 'WEATHER_CONDITION'), ('ROAD_CONDITION', 'ROAD_CONDITION'))


# Create your models here.
class Occurrence(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=5000, blank=True, default='')
    state = models.CharField(choices=STATE_CHOICES, default='POR VALIDAR', blank=False, max_length=15)
    category = models.CharField(choices=CATEGORY_CHOICES, blank=False, max_length=30)

    class Meta:
        ordering = ('updated',)
