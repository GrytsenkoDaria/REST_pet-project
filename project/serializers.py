from rest_framework import serializers

from project.models import Project, ProjectUser
from user.serializers import UserListSerializer


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'status']
        extra_kwargs = {'status': {
            'default': 0,
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
