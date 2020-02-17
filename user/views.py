from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import User


class UserCreationView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLogout(generics.GenericAPIView):

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_no_content)
