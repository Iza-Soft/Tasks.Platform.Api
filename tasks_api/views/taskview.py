from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from datetime import datetime

from tasks_api import serializers
from tasks_api import models

class TaskApiView(APIView):
    """Handle creating and extracting Tasks"""

    def get(self, request, *args, **kwargs):
        """List all the task items"""

        task = models.Task.objects.all()

        serializer = serializers.TaskSerializer(task, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Create new task item"""

        data = {
            'name': request.data.get('name'),
            'status': request.data.get('status'),
            'description': request.data.get('description'),
            'workspace_id': request.data.get('workspace_id')
        }

        serializer = serializers.TaskSerializer(data= data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)