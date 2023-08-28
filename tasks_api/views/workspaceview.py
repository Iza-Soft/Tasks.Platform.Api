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
from tasks_api.core.workspace.responsewrapper import ResponseWrapper

class WorkSpaceApiView(APIView):
    """Handle creating and extracting Work-Space"""

    def get(self, request, *args, **kwargs):
        """List all the worksspace items"""

        task = models.WorkSpace.objects.all()

        serializer = serializers.WorkSpaceSerializer(task, many=True)

        wrapper = ResponseWrapper()

        return Response(wrapper.responseModel(serializer.data), status= status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        """Create new workspace item"""

        data = {
            'name': request.data.get('name')
        }

        serializer = serializers.WorkSpaceSerializer(data= data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class WorkSpaceDetailsApiView(APIView):   
    """Handle updating, deleting and retrieving a specific workspace"""

    def get_object(self, workspace_id):
        """Helper method to get the object with given workspace_id"""

        try:
            return models.WorkSpace.objects.get(id=workspace_id)
        except models.WorkSpace.DoesNotExist:
            return None

    def get(self, request, workspace_id, *args, **kwargs):
        """Retrieves the workspace item with given task_id"""

        workspace_object = self.get_object(workspace_id)

        if not workspace_object:
            return Response({"message": f"Object with id {workspace_id} does not exists"}, status= status.HTTP_404_NOT_FOUND)
        
        serializer = serializers.WorkSpaceSerializer(workspace_object)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def put(self, request, workspace_id, *args, **kwargs):
        """Handle updating workspace item with given workspace_id if exists"""

        workspace_object = self.get_object(workspace_id)

        if not workspace_object:
            return Response({"message": f"Object with ${workspace_id} does not exists"}, status= status.HTTP_404_NOT_FOUND)
        
        data = {
            'name': request.data.get('name'),
            'total_task_count': request.data.get('total_task_count'),
            'bgcolor': request.data.get('bgcolor'),
            'updated_at': datetime.now()
        }

        serializer = serializers.WorkSpaceSerializer(instance= workspace_object, data= data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, workspace_id, *args, **kwargs):
        """Handle deleting workspace item with given workspace_id if exists"""

        workspace_object = self.get_object(workspace_id)

        if not workspace_object:
            return Response({"message": f"Object with ${taks_id} does not exists"}, status= status.HTTP_404_NOT_FOUND)
        
        workspace_object.delete()
        return Response({"message": "object deleted!"}, status=status.HTTP_200_OK)