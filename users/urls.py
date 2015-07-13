from django.conf.urls import url

from .views import UserCurrent, UserDetail, UserList

urlpatterns = [
    url(
        regex=r"^users$",
        view=UserList.as_view(),
        name="list"),
    url(
        regex=r"^users/(?P<pk>\d+)$",
        view=UserDetail.as_view(),
        name="detail"),
    url(
        regex=r"^users/current$",
        view=UserCurrent.as_view(),
        name="current"),
]
