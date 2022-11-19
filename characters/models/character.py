from django.db import models
from .voice_actor import VoiceActor

# Create your models here.

class Character(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    voice_actor = models.ForeignKey(
        VoiceActor,
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} has the job {self.occupation} and is played by {self.voice_actor}'
