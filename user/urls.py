from django.conf.urls import url
from user.views import UserList

urlpatterns = [
    url(r'', UserList.as_view()),
]
