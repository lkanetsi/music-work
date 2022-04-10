from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from app.models import MusicalWork
from .serializers import MusicalWorkSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000

class MusicCompositionApiView(generics.ListAPIView):
    '''Endpoint for for fetching musical works by ISWC'''
    queryset = MusicalWork.objects.all()
    serializer_class = MusicalWorkSerializer
    lookup_field = 'iswc'
    
class MusicCompositionListingApiView(generics.ListAPIView):
    '''Endpoint for listing musical works and includes pagiantion to reduce response time'''
    queryset = MusicalWork.objects.all()
    serializer_class = MusicalWorkSerializer
    lookup_field = 'iswc'
    pagination_class = LargeResultsSetPagination