from django.conf.urls import url
from rest_framework.authtoken import views

from user.views import UserLogout, UserCreationView

urlpatterns = [
    url(r'^registration/', UserCreationView.as_view()),
    url(r'^login/', views.obtain_auth_token),
    url(r'^logout/', UserLogout.as_view()),
]
