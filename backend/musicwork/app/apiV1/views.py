from rest_framework import generics
from app.models import MusicalWork
from .serializers import MusicalWorkSerializer


class MusicCompositionApiView(generics.ListAPIView):
    '''Endpoint for listing musical works by ISWC'''
    queryset = MusicalWork.objects.all()
    serializer_class = MusicalWorkSerializer
    lookup_field = 'iswc'
