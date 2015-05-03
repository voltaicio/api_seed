from django.conf.urls import url

from .views import ThingDetail, ThingList

urlpatterns = [
    url(r'^things/(?P<pk>\d+)$', ThingDetail.as_view(), name="thing_detail"),
    url(r'^things$', ThingList.as_view(), name="thing_list"),
]
