from django.conf.urls import url

from .views import ThingDetail, ThingList

urlpatterns = [
    url(
        regex=r'^things/(?P<pk>\d+)$',
        view=ThingDetail.as_view(),
        name="thing_detail"),
    url(
        regex=r'^things$',
        view=ThingList.as_view(),
        name="thing_list"),
]
