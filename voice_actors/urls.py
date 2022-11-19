from django.urls import path
from .views.voice_actor_views import VoiceActorView, VoiceActorDetailView

urlpatterns = [
    path('', VoiceActorView.as_view(), name='voice-actor'),
    path('<int:pk>/', VoiceActorDetailView.as_view(), name='voice-actor'),
]