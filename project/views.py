from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import ProjectDetailSerializer, ProjectSerializer
from .serializers import ReleaseDetailSerializer, ReleaseSerializer
from .serializers import SprintDetailSerializer, SprintSerializer
from .models import Project, Release, Sprint
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


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
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
    serializer_class = ReleaseSerializer

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
                project_id=project_id,
            )

        return queryset


class ReleaseDetailView(generics.RetrieveUpdateDestroyAPIView):
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


class SprintListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrSuperuserOrManager]
    serializer_class = SprintSerializer

    def get_queryset(self):

        release_id = self.kwargs.get('release_pk')

        if (
            self.request.user.role == Role.ADMIN or
            self.request.user.is_superuser
        ):
            queryset = Sprint.objects.filter(release_id=release_id)

        else:
            user = self.request.user
            projects = user.projects.all()
            project_id = self.kwargs.get('project_pk')
            releases = Release.objects.filter(
                project__in=projects,
                project_id=project_id
            )
            queryset = Sprint.objects.filter(
                release_id=release_id,
                release__in=releases,
                )

        return queryset


class SprintDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrSuperuserOrManager]
    serializer_class = SprintDetailSerializer

    def get_queryset(self):

        release_id = self.kwargs.get('release_pk')

        if (
            self.request.user.role == Role.ADMIN or
            self.request.user.is_superuser
        ):
            queryset = Sprint.objects.filter(release_id=release_id)

        else:
            user = self.request.user
            projects = user.projects.all()
            project_id = self.kwargs.get('project_pk')
            releases = Release.objects.filter(
                project__in=projects,
                project_id=project_id
            )
            queryset = Sprint.objects.filter(
                release_id=release_id,
                release__in=releases,
                )

        return queryset


class SprintProjectListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrSuperuserOrManager]
    serializer_class = SprintSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')

        if (
            self.request.user.role == Role.ADMIN or
            self.request.user.is_superuser
        ):
            releases = Release.objects.filter(project_id=project_id)
            queryset = Sprint.objects.filter(release__in=releases)

        else:
            user = self.request.user
            projects = user.projects.all()
            releases = Release.objects.filter(
                project__in=projects,
                project_id=project_id
            )
            queryset = Sprint.objects.filter(
                release__in=releases,
                )

        return queryset
