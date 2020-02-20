from django.urls import path

from project.views import ProjectListView, ProjectDetailsView

urlpatterns = [
    path('<int:pk>/', ProjectDetailsView.as_view()),
    path('', ProjectListView.as_view()),
]
