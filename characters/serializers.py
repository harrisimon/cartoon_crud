from rest_framework import serializers

from .models.character import Character
from .models.voice_actor import VoiceActor

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Character

class CharacterPlayedSerializer(serializers.ModelSerializer):
    voice_actor = serializers.StringRelatedField()
    class Meta:
        fields = '__all__'
        model = Character



class VoiceActorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = VoiceActor