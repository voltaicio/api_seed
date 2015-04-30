from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r"^v1/api-token-auth", "rest_framework_jwt.views.obtain_jwt_token"),
    url(r"^grappelli/", include("grappelli.urls")),
    url(r'^admin/', include(admin.site.urls)),
]
