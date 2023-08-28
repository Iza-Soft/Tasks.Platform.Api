from django.core.validators import MaxValueValidator
from django.db import models

class WorkSpace(models.Model):
    """DataBase model for workspace in the systems"""

    class Meta:
        db_table = 'workspace'
        ordering = ['-created_at']

    name = models.CharField(max_length=255)
    total_task_count = models.PositiveSmallIntegerField(default=0, blank=True, validators=[MaxValueValidator(100)])
    bgcolor = models.CharField(max_length= 10, blank=True, null=False, default = '806885')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    def __str__(self):
        """Retrieve object representation of our workspace"""
        return self.name

class Task(models.Model):
    """DataBase model for task in the systems"""

    class Meta:
        db_table = 'task'
        ordering = ['-created_at']

    name = models.CharField(max_length=255)
    status = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    workspace_id = models.ForeignKey(WorkSpace, on_delete=models.CASCADE, null=True, blank=True, related_name='tasks', db_column="workspace_id")

    def __str__(self):
        """Retrieve object representation of our task"""
        return self.name