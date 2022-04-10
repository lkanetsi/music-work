from django.contrib import admin
from .models import MusicalWork


class MuscialWorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'contributors', 'iswc']

admin.site.register(MusicalWork,MuscialWorkAdmin)