from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(
        r"^v1/api-token-auth", "rest_framework_jwt.views.obtain_jwt_token",
        name="api_token_auth"),
    url(r"^v1/", include("core.urls", namespace="core")),
    url(r"^v1/", include("users.urls", namespace="users")),
    url(r"^grappelli/", include("grappelli.urls")),
    url(r'^admin/', include(admin.site.urls)),
]
