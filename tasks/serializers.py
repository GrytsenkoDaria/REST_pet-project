from rest_framework import serializers

from tasks.models import Task
from project.serializers import (
    ProjectSerializer,
    ReleaseSerializer,
    SprintSerializer
)
from user.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'status', 'initiator', ]
        extra_kwargs = {
            'status': {'default': 0, },
        }

    def create(self, validated_data):
        sprint_id = self.context['view'].kwargs['pk']
        project_id = self.context['view'].kwargs['project_pk']
        release_id = self.context['view'].kwargs['release_pk']
        initiator_id = self.context['request'].user.id

        validated_data['sprint_id'] = sprint_id
        validated_data['project_id'] = project_id
        validated_data['release_id'] = release_id
        validated_data['initiator_id'] = initiator_id

        task = super().create(validated_data)
        return task


class TaskDetailSerializer(serializers.ModelSerializer):
    assignee = UserSerializer()
    initiator = UserSerializer()
    project = ProjectSerializer()
    release = ReleaseSerializer()
    sprint = SprintSerializer()
    parent_task = TaskSerializer()

    class Meta:
        model = Task
        fields = '__all__'

        extra_kwargs = {
            'status': {'default': 0, },
        }
