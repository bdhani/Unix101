from rest_framework import viewsets 
from .models import Command
from .serializers import CommandSerializer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

class CommandViewSet(viewsets.ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer

    def create(self, request, *args, **kwargs):
        print(f"Received data: {request.data}")  # Debugging line
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    @action(detail=False, methods=['get'])
    def search(self, request):
        keyword = request.query_params.get('search', None)
        if keyword is not None:
            commands = Command.objects.filter(name__icontains=keyword) | Command.objects.filter(description__icontains=keyword)
            serializer = self.get_serializer(commands, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "No keyword provided"}, status=status.HTTP_400_BAD_REQUEST)

def all_commands(request):
    return HttpResponse('Returning all commands')







