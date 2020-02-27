from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer, TaskDetailSerializer
from user.permissions import IsAdminOrSuperuser
from choices import Role
from project.models import Release, Sprint


class TaskListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrSuperuser]
    serializer_class = TaskSerializer

    def get_queryset(self):

        project_id = self.kwargs.get('project_pk')
        release_id = self.kwargs.get('release_pk')
        sprint_id = self.kwargs.get('pk')

        queryset = Task.objects.none()

        if (
            self.request.user.role == Role.ADMIN or
            self.request.user.is_superuser
        ):
            release_ids = (
                Release.objects
                .filter(project_id=project_id)
                .values_list('id', flat=True)
            )

            if release_id in release_ids:
                sprint_ids = (
                    Sprint.objects
                    .filter(release_id=release_id)
                    .values_list('id', flat=True)
                )

                if sprint_id in sprint_ids:
                    queryset = Task.objects.filter(sprint_id=sprint_id)

        else:
            user = self.request.user
            projects = user.projects.all()

            release_ids = (
                Release.objects
                .filter(
                    project__in=projects,
                    project_id=project_id
                )
                .values_list('id', flat=True)
            )

            if release_id in release_ids:
                sprint_ids = (
                    Sprint.objects
                    .filter(release_id=release_id)
                    .values_list('id', flat=True)
                )

                if sprint_id in sprint_ids:
                    queryset = Task.objects.filter(sprint_id=sprint_id)

        return queryset


class TaskDetailView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrSuperuser]
    serializer_class = TaskDetailSerializer

    def get_queryset(self):

        project_id = self.kwargs.get('project_pk')
        release_id = self.kwargs.get('release_pk')
        sprint_id = self.kwargs.get('sprint_pk')
        task_id = self.kwargs.get('pk')

        queryset = Task.objects.none()

        if (
            self.request.user.role == Role.ADMIN or
            self.request.user.is_superuser
        ):
            release_ids = (
                Release.objects
                .filter(project_id=project_id)
                .values_list('id', flat=True)
            )

            if release_id in release_ids:
                sprint_ids = (
                    Sprint.objects
                    .filter(release_id=release_id)
                    .values_list('id', flat=True)
                )

                if sprint_id in sprint_ids:
                    task_ids = (
                        Task.objects
                        .filter(sprint_id=sprint_id)
                        .values_list('id', flat=True)
                    )

                    if task_id in task_ids:
                        queryset = Task.objects.filter(id=task_id)

        else:
            user = self.request.user
            projects = user.projects.all()

            release_ids = (
                Release.objects
                .filter(
                    project__in=projects,
                    project_id=project_id
                )
                .values_list('id', flat=True)
            )

            if release_id in release_ids:
                sprint_ids = (
                    Sprint.objects
                    .filter(release_id=release_id)
                    .values_list('id', flat=True)
                )

                if sprint_id in sprint_ids:
                    task_ids = (
                        Task.objects
                        .filter(sprint_id=sprint_id)
                        .values_list('id', flat=True)
                    )

                    if task_id in task_ids:
                        queryset = Task.objects.filter(id=task_id)

                    queryset = Task.objects.filter(id=task_id)

        return queryset


class TaskListFilterView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrSuperuser]
    serializer_class = TaskSerializer

    def get_queryset(self):

        project_id = self.kwargs.get('pk')

        queryset = Task.objects.none()

        if (
            self.request.user.role == Role.ADMIN or
            self.request.user.is_superuser
        ):
            releases = Release.objects.filter(project_id=project_id)
            sprints = Sprint.objects.filter(release__in=releases, )

            queryset = Task.objects.filter(sprint__in=sprints, )

            release_id = self.request.query_params.get('release_id', None)
            sprint_id = self.request.query_params.get('sprint_id', None)

            if release_id is not None:
                queryset = queryset.filter(release_id=release_id)
            elif sprint_id is not None:
                queryset = queryset.filter(sprint_id=sprint_id)

        else:
            user = self.request.user
            projects = user.projects.all()

            releases = Release.objects.filter(
                project__in=projects,
                project_id=project_id
            )
            sprints = Sprint.objects.filter(release__in=releases, )

            queryset = Task.objects.filter(sprint__in=sprints, )

            release_id = self.request.query_params.get('release_id', None)
            sprint_id = self.request.query_params.get('sprint_id', None)

            if release_id is not None:
                queryset = queryset.filter(release_id=release_id)
            elif sprint_id is not None:
                queryset = queryset.filter(sprint_id=sprint_id)

        return queryset


class TaskDetailFilterView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrSuperuser, IsAuthenticated]
    serializer_class = TaskDetailSerializer

    def get_queryset(self):

        project_id = self.kwargs.get('project_pk')
        task_id = self.kwargs.get('pk')

        queryset = Task.objects.none()

        if (
            self.request.user.role == Role.ADMIN or
            self.request.user.is_superuser
        ):
            releases = Release.objects.filter(project_id=project_id)
            sprints = Sprint.objects.filter(release__in=releases, )

            queryset = Task.objects.filter(sprint__in=sprints, )

            release_id = self.request.query_params.get('release_id', None)
            sprint_id = self.request.query_params.get('sprint_id', None)

            if release_id is not None:
                queryset = queryset.filter(release_id=release_id)
            elif sprint_id is not None:
                queryset = queryset.filter(sprint_id=sprint_id)

        else:
            user = self.request.user
            projects = user.projects.all()

            releases = Release.objects.filter(
                project__in=projects,
                project_id=project_id
            )
            sprints = Sprint.objects.filter(release__in=releases, )

            queryset = Task.objects.filter(
                sprint__in=sprints,
                id=task_id,
            )

            release_id = self.request.query_params.get('release_id', None)
            sprint_id = self.request.query_params.get('sprint_id', None)

            if release_id is not None:
                queryset = queryset.filter(release_id=release_id)
            elif sprint_id is not None:
                queryset = queryset.filter(sprint_id=sprint_id)

        return queryset
