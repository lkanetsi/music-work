from django.db import models
from simple_history.models import HistoricalRecords


class MusicalWork(models.Model):

    """ musical compostion metadata records"""

    title = models.CharField(max_length=255)
    contributors = models.CharField(max_length=255)
    iswc = models.CharField(max_length=30)
    history = HistoricalRecords()
    created_at = models.DateTimeField(auto_now_add=True,)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


