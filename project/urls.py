from django.urls import path

from project.views import ProjectListView, ProjectDetailView
from project.views import ReleaseListView, ReleaseDetailView
from project.views import SprintListView, SprintDetailView
from project.views import SprintProjectListView
from tasks.views import TaskListView, TaskDetailView
from tasks.views import TaskListFilterView, TaskDetailFilterView

urlpatterns = [
    path('', ProjectListView.as_view()),
    path('<int:pk>/', ProjectDetailView.as_view()),
    path('<int:project_pk>/releases/', ReleaseListView.as_view()),

    path(
        '<int:project_pk>/releases/<int:pk>/',
        ReleaseDetailView.as_view()
    ),

    path(
        '<int:project_pk>/releases/<int:release_pk>/sprints/',
        SprintListView.as_view()
    ),

    path(
        '<int:project_pk>/releases/<int:release_pk>/sprints/<int:pk>/',
        SprintDetailView.as_view()
    ),

    path(
        '<int:project_pk>/sprints/',
        SprintProjectListView.as_view()
    ),

    path(
        '<int:project_pk>/releases/<int:release_pk>/sprints/<int:pk>/tasks/',
        TaskListView.as_view()
    ),

    path(
        '<int:project_pk>/releases/<int:release_pk>/sprints/<int:sprint_pk>/tasks/<int:pk>/',
        TaskDetailView.as_view()
    ),

    path(
        # '<int:pk>/tasks/?release_id=<release_id>&sprint_id=<sprint_id>/',
        '<int:pk>/tasks/',
        TaskListFilterView.as_view()
    ),

    path(
        # '<int:pk>/tasks/?release_id=<release_id>&sprint_id=<sprint_id>/',
        '<int:project_pk>/tasks/<int:pk>/',
        TaskDetailFilterView.as_view()
    ),

]
