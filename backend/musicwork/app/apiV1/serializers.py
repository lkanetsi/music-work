from rest_framework import serializers 
from app.models import MusicalWork

class MusicalWorkSerializer( serializers.ModelSerializer ):

    class Meta:
        model = MusicalWork
        fields = '__all__'


