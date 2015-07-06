from django.contrib.auth import get_user_model

from rest_framework import generics

from .filters import UserFilter
from .serializers import UserSerializer

User = get_user_model()


class UserMixin(object):
    """
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(UserMixin, generics.RetrieveUpdateAPIView):
    """
    """

    pass


class UserList(UserMixin, generics.ListCreateAPIView):
    """
    """

    filter_class = UserFilter
    search_fields = ("email",)
