from rest_framework import generics

from .models import Thing
from .serializers import ThingSerializer


class ThingMixin(object):
    """
    """

    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class ThingDetail(ThingMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    """

    pass


class ThingList(ThingMixin, generics.ListCreateAPIView):
    """
    """

    pass
