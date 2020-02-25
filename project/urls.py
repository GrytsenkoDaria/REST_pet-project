from django.urls import path

from project.views import ProjectListView, ProjectDetailView
from project.views import ReleaseListView, ReleaseDetailView
from project.views import SprintListView, SprintDetailView
from project.views import SprintProjectListView

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

]
