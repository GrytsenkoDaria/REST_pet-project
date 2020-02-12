from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer


class UserList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
