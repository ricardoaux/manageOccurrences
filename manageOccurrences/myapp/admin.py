from django.contrib import admin
from manageOccurrences.myapp.models import Occurrence


# Register your models here.
class OccurrenceAdmin(admin.ModelAdmin):
    list_display = ("created", 'updated', 'category', 'state', 'author')


admin.site.register(Occurrence, OccurrenceAdmin)
