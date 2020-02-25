from rest_framework import serializers

from project.models import Project, ProjectUser, Release
from user.serializers import UserListSerializer


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'status']
        extra_kwargs = {'status': {
            'write_only': True,
            'required': False
            }
        }

    def create(self, *args, **kwargs):
        project = super().create(*args, **kwargs)
        ProjectUser.objects.create(
            project=project,
            user=self.context['request'].user,
            is_owner=True
        )
        return project


class ProjectDetailSerializer(serializers.ModelSerializer):
    users = UserListSerializer(many=True, read_only=True)

    class Meta:
        lookup_field = 'id'
        model = Project
        fields = ['id', 'name', 'status', 'users']


class ReleaseListSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(required=True)
    end_time = serializers.DateTimeField(required=True)

    class Meta:
        model = Release
        fields = ['id', 'name', 'status', 'start_time', 'end_time', ]
        extra_kwargs = {
            'status': {'write_only': True, 'required': False},
            'start_time': {'write_only': True},
            'end_time': {'write_only': True},
        }

    def create(self, validated_data):
        project_id = self.context['view'].kwargs.get('project_pk')
        validated_data['project_id'] = project_id
        release = super().create(validated_data)
        return release


class ReleaseDetailSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()

    class Meta:
        lookup_field = 'id'
        model = Release
        fields = ['id', 'name', 'status', 'project', 'start_time', 'end_time']
