from django.shortcuts import render, get_object_or_404
from ..serializers import VoiceActorSerializer
from ..models.voice_actor import VoiceActor
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class VoiceActorView(APIView):
        """View class for voice actors / viewing all and creating"""
        serializer_class = VoiceActorSerializer
        def get(self, request):
            voice_actors = VoiceActor.objects.all()
            serializer = VoiceActorSerializer(voice_actors, many = True)
            return Response({'voice_actors': serializer.data})

        def post(self, request):
            serializer = VoiceActorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.erorrs, status=status.HTTP_400_BAD_REQUEST)

class VoiceActorDetailView(APIView):
    """View class for voice_actors/:pk for viewing a single voice actor, updating a single voice actors, or removing a single character"""
    serializer_class = VoiceActorSerializer
    def get(self, request, pk):
        voice_actor = get_object_or_404(VoiceActor, pk=pk)
        serializer = VoiceActorSerializer(voice_actor, data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        voice_actor = get_object_or_404(VoiceActor, pk=pk)
        serializer = VoiceActorSerializer(voice_actor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
