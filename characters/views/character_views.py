from django.shortcuts import render, get_object_or_404
from ..serializers import CharacterSerializer, CharacterReadSerializer
from ..models.character import Character
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class CharacterView(APIView):
    """View class for characters / viewing all and creating"""
    serializer_class = CharacterSerializer
    def get(self, request):
        characters = Character.objects.all()
        serializer = CharacterReadSerializer(characters, many = True)
        return Response({'characters': serializer.data})

    def post(self, request):
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.erorrs, status=status.HTTP_400_BAD_REQUEST)


class CharacterDetailView(APIView):
        """View class for characters/:pk for viewing a single character, updating a single character, or removing a single character"""
        serializer_class = CharacterSerializer
        def get(self, request, pk):
            character = get_object_or_404(Character, pk=pk)
            serializer = CharacterPlayedSerializer(character)
            return Response({'character':serializer.data})


        def put(self, request, pk):
            character = get_object_or_404(Character, pk=pk)
            serializer = CharacterSerializer(character, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk):
            character = get_object_or_404(Character, pk=pk)
            character.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)