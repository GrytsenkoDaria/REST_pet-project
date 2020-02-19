from django.urls import path
from rest_framework.authtoken import views

from user.views import UserLogout, UserCreationView

urlpatterns = [
    path('registration/', UserCreationView.as_view()),
    path('login/', views.obtain_auth_token),
    path('logout/', UserLogout.as_view()),
]
