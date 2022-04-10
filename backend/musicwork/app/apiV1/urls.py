from django.urls import path
from .views import MusicCompositionApiView,MusicCompositionListingApiView

urlpatterns = [
    path('', MusicCompositionListingApiView.as_view(), name='musicalcomp-listing'),
    path('all-works/<str:iswc>', MusicCompositionListingApiView.as_view(), name='musicalcomp-listing')
]
