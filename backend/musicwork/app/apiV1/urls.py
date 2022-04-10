from django.urls import path
from .views import MusicCompositionApiView,MusicCompositionListingApiView

urlpatterns = [
    path('', MusicCompositionApiView.as_view(), name='musicalcomp-listing'),
    path('all-works/', MusicCompositionListingApiView.as_view(), name='musicalcomp-listing')
]
