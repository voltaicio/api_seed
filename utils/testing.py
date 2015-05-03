import json

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase


User = get_user_model()


class BaseAPITestCase(APITestCase):
    """
    """

    username = "admin@test.com"
    password = "adm1n"
    token = None

    @classmethod
    def setUpClass(cls):
        """
        """

        cls.user, created = User.objects.get_or_create(
            username=cls.username,
            defaults={
                "is_active": True,
                "is_staff": True,
                "is_superuser": True,
                "password": make_password(cls.password)
            })

        super(BaseAPITestCase, cls).setUpClass()

    def authenticate(self):
        """
        """

        if self.token is None:
            response = self.client.post(reverse("api_token_auth"), {
                "username": self.username,
                "password": self.password
            })
            BaseAPITestCase.token = json.loads(
                response.content.decode("utf-8"))["token"]

        self.client.credentials(HTTP_AUTHORIZATION="JWT " + self.token)
