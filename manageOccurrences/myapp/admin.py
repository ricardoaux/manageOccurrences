from django.contrib import admin
from manageOccurrences.myapp.models import Occurrence

"""
    Permite a gestão das ocorrencias na pagina de administracao
"""


class OccurrenceAdmin(admin.ModelAdmin):
    list_display = ("created", 'updated', 'category', 'state', 'author')


admin.site.register(Occurrence, OccurrenceAdmin)
