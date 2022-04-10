from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from app.models import MusicalWork
from .serializers import MusicalWorkSerializer


class LargeResultsSetPagination(PageNumberPagination):
    '''pagination for listing musical works with the limit of 100 per request'''
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class MusicCompositionApiView(generics.ListAPIView):
    '''Endpoint for fetching musical works by filtering with ISWC,contributors and title'''
    queryset = MusicalWork.objects.all()
    serializer_class = MusicalWorkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title','iswc','contributors']
    
class MusicCompositionListingApiView(generics.ListAPIView):
    '''Endpoint for listing musical works and includes pagiantion to reduce response time'''
    queryset = MusicalWork.objects.all()
    serializer_class = MusicalWorkSerializer
    lookup_field = 'iswc'
    pagination_class = LargeResultsSetPagination