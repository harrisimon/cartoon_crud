from rest_framework import serializers

from .models.character import Character
from .models.show import Show
from .models.voice_actor import VoiceActor

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Character

class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Show

class VoiceActorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = VoiceActor