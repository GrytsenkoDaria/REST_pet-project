from django.urls import path

from project.views import ProjectListView, ProjectDetailsView
from project.views import ReleaseListView, ReleaseDetailsView

urlpatterns = [
    path('', ProjectListView.as_view()),
    path('<int:pk>/', ProjectDetailsView.as_view()),
    path('<int:project_pk>/releases/', ReleaseListView.as_view()),
    path('<int:project_pk>/releases/<int:pk>/', ReleaseDetailsView.as_view()),
]
