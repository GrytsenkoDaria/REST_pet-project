from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import ProjectDetailSerializer, ProjectListSerializer
from .serializers import ReleaseDetailSerializer, ReleaseListSerializer
from .models import Project, Release
from choices import Role
from user.permissions import IsAdminOrSuperuser


class ProjectListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrSuperuser]
    serializer_class = ProjectListSerializer

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
    permission_classes = [IsAuthenticated, IsAdminOrSuperuser, ]
    serializer_class = ReleaseListSerializer

    def get_queryset(self):
        if (
            self.request.user.role == Role.ADMIN or
            self.request.user.is_superuser
        ):
            queryset = Release.objects.all()
        elif self.request.user.role == Role.MANAGER:
            user = self.request.user
            queryset = user.releases.all()

        return queryset
