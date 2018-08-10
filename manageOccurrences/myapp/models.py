from django.contrib.auth.models import User
from django.db import models

STATE_CHOICES = (('POR VALIDAR', 'POR VALIDAR'), ('VALIDADO', 'VALIDADO'), ('RESOLVIDO', 'RESOLVIDO'))
CATEGORY_CHOICES = (('CONSTRUCTION', 'CONSTRUCTION'), ('SPECIAL_EVENT', 'SPECIAL_EVENT'), ('INCIDENT', 'INCIDENT'),
                    ('WEATHER_CONDITION', 'WEATHER_CONDITION'), ('ROAD_CONDITION', 'ROAD_CONDITION'))

"""
    Modelo de dados relativo as ocorrencias
"""
class Occurrence(models.Model):
    # uma ocorrencia tem sempre autor, dai a relacao de chave estrangeira
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # automaticamente a data de criacao e gerada
    created = models.DateTimeField(auto_now_add=True)
    # automaticamente, a cada update a data e atualizada
    updated = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=5000, blank=True, default='')
    # os dois proximos campos estao dependentes dos valores predefinidos para escolha
    state = models.CharField(choices=STATE_CHOICES, default='POR VALIDAR', blank=False, max_length=15)
    category = models.CharField(choices=CATEGORY_CHOICES, blank=False, max_length=30)

    class Meta:
        ordering = ('updated',)

