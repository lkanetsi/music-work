from django.db import models
from simple_history.models import HistoricalRecords

class MusicalWork(models.Model):
    """Model for musical compostion metadata"""
    title = models.CharField(max_length=255)
    contributors = models.CharField(max_length=255)
    iswc = models
    history = HistoricalRecords()
    
    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title 