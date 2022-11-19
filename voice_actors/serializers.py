from rest_framework import serializers

from .models.voice_actor import VoiceActor

class VoiceActorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = VoiceActor