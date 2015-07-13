from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import UserFilter
from .serializers import UserSerializer

User = get_user_model()


class UserMixin(object):
    """
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCurrent(APIView):
    """
    """

    def get(self, request):
        """
        Creates a simple response consisting of the currently authenticated
        user.
        """

        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class UserDetail(UserMixin, generics.RetrieveUpdateAPIView):
    """
    """

    pass


class UserList(UserMixin, generics.ListCreateAPIView):
    """
    """

    filter_class = UserFilter
    search_fields = ("email",)
