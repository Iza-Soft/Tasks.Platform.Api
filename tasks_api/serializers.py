from rest_framework import serializers
from tasks_api import models
from rest_framework.serializers import ListSerializer


class TaskSerializer(serializers.ModelSerializer):
    """Serializer a Task object"""

    class Meta:
        model = models.Task
        fields = ('id', 'name', 'status', 'description', 'created_at', 'updated_at', 'workspace_id')
        extra_kwargs = {'workspace_id': {'required': True}}

    def create(self, validated_data):
        task = models.Task.objects.create(**validated_data)

        task_count = models.Task.objects.filter(workspace_id=validated_data.get('workspace_id')).count()

        workspace = models.WorkSpace.objects.get(id=validated_data.get('workspace_id').id)
        workspace.total_task_count = task_count
        workspace.save(update_fields=['total_task_count'])
        
        #models.WorkSpace.objects.update(id = validated_data.get('workspace_id').id, total_task_count = task_count)

        return task

class WorkSpaceSerializer(serializers.ModelSerializer):
    """Serializer a workspace object"""
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = models.WorkSpace
        fields = ('id', 'name', 'total_task_count', 'bgcolor', 'created_at', 'updated_at', 'tasks')
        extra_kwargs = {'tasks': {'required': False}}
