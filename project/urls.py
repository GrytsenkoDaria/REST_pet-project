from django.urls import path

from project.views import ProjectListView, ProjectDetailsView
from project.views import ReleaseListView

urlpatterns = [
    path('<int:pk>/', ProjectDetailsView.as_view()),
    path('', ProjectListView.as_view()),
    path('<int:project_pk>/release/', ReleaseListView.as_view()),
    path('<int:project_pk>/release/<int:pk>', ProjectListView.as_view()),
]
