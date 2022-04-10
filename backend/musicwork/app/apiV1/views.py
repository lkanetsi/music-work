from rest_framework import generics
from app.models import MusicalWork
from .serializers import MusicalWorkSerializer


class MusicCompositionApiView(generics.ListCreateAPIView):
    '''Endpoint for listing musical composition metadata'''
    queryset = MusicalWork.objects.all()
    serializer_class = MusicalWorkSerializer
