from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from users.models import User
from users.serializers import UsersSerializers, UsersCreateSerializers,\
    UsersUpdateSerializers



class UsersListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializers

class UsersDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializers

class UsersCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersCreateSerializers

class UsersUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersUpdateSerializers


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


def obtain_auth_token(request):
    return None
