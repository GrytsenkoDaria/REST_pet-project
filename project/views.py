from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import ProjectDetailSerializer, ProjectSerializer
from .serializers import ReleaseDetailSerializer, ReleaseListSerializer
from .models import Project, Release
from choices import Role
from user.permissions import IsAdminOrSuperuser, IsAdminOrSuperuserOrManager


class ProjectListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrSuperuser]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        if (
            self.request.user.role == Role.ADMIN or
            self.request.user.is_superuser
        ):
            queryset = Project.objects.all()
        else:
            user = self.request.user
            queryset = user.projects.all()
        return queryset


class ProjectDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrSuperuser]
    serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        if (
            self.request.user.role == Role.ADMIN or
            self.request.user.is_superuser
        ):
            queryset = Project.objects.all()
        else:
            user = self.request.user
            queryset = user.projects.all()

        return queryset


class ReleaseListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrSuperuserOrManager, ]
    serializer_class = ReleaseListSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')

        if (
            self.request.user.role == Role.ADMIN or
            self.request.user.is_superuser
        ):
            queryset = Release.objects.filter(project_id=project_id)

        else:
            user = self.request.user
            projects = user.projects.all()
            queryset = user.releases.filter(
                project__in=projects,
                project_id=project_id,
            )

        return queryset


class ReleaseDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrSuperuserOrManager, ]
    serializer_class = ReleaseDetailSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')

        if (
            self.request.user.role == Role.ADMIN or
            self.request.user.is_superuser
        ):
            queryset = Release.objects.filter(project_id=project_id)

        else:
            user = self.request.user
            projects = user.projects.all()
            queryset = Release.objects.filter(
                project__in=projects,
                project_id=project_id
            )

        return queryset
