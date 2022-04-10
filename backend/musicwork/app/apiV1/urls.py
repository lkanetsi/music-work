from django.urls import path
from .views import MusicCompositionApiView

urlpatterns = [
    path('', MusicCompositionApiView.as_view(), name='musicalcomp-listing')
]
