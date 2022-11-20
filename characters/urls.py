from django.urls import path
from .views.character_views import CharacterView, CharacterDetailView
from .views.show_views import ShowView, ShowDetailView
from .views.voice_actor_views import VoiceActorView, VoiceActorDetailView

urlpatterns = [
    path('characters/', CharacterView.as_view(), name='characters'),
    path('characters/<int:pk>/', CharacterDetailView.as_view(), name='character'),
    path('shows/', ShowView.as_view(), name='shows'),
    path('shows/<int:pk>/', ShowDetailView.as_view(), name='show'),
    path('voice-actors/', VoiceActorView.as_view(), name='voice-actors'),
    path('voice-actors/<int:pk>/', VoiceActorDetailView.as_view(), name='voice-actor')
]