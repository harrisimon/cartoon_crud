from django.shortcuts import render, get_object_or_404
from ..serializers import ShowSerializer
from ..models.show import Show
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class ShowView(APIView):
    """View class for shows / viewing all and creating"""
    serializer_class = ShowSerializer
    def get(self, request):
        shows = Show.objects.all()
        serializer = ShowSerializer(shows, many = True)
        return Response({'shows': serializer.data})

    def post(self, request):
        serializer = ShowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.erorrs, status=status.HTTP_400_BAD_REQUEST)

class ShowDetailView(APIView):
    """View class for shows/:pk for viewing a single show, updating a single show, or removing a single show"""
    serializer = ShowSerializer
    def get(self, request, pk):
        show = get_object_or_404(Show, pk=pk)
        serializer = ShowSerializer(show, data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        show = get_object_or_404(Show, pk=pk)
        show.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)