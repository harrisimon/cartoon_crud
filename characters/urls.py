from django.urls import path
from .views.character_views import CharacterView, CharacterDetailView

urlpatterns = [
    path('', CharacterView.as_view(), name='characters'),
    path('<int:pk>/', CharacterDetailView.as_view(), name='characters'),
]