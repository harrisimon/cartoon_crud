from django.db import models
from .voice_actor import VoiceActor

# Create your models here.

class Character(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    voiced_by = models.ForeignKey(
        VoiceActor,
        on_delete=models.CASCADE,
        related_name='character_played'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} has the job {self.occupation}'
