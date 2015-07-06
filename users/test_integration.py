from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict

from .factories import UserFactory
from utils.testing import BaseAPITestCase


class UserDetailTest(BaseAPITestCase):
    """
    Tests the 'users:detail' endpoint.
    """

    def test_get_unauthenticated(self):
        """401"""

        response = self.client.get(
            reverse("users:detail", kwargs={"pk": 0}))
        self.assertEqual(response.status_code, 401)

    def test_get_object_does_not_exist(self):
        """404"""

        self.authenticate()
        response = self.client.get(
            reverse("users:detail", kwargs={"pk": 0}))
        self.assertEqual(response.status_code, 404)

    def test_get_ok(self):
        """200"""

        o = UserFactory.create()

        self.authenticate()
        response = self.client.get(
            reverse("users:detail", kwargs={"pk": o.id}))
        self.assertEqual(response.status_code, 200)

    def test_patch_unauthenticated(self):
        """401"""

        response = self.client.patch(
            reverse("users:detail", kwargs={"pk": 0}), {})
        self.assertEqual(response.status_code, 401)

    def test_patch_object_does_not_exist(self):
        """404"""

        self.authenticate()
        response = self.client.patch(
            reverse("users:detail", kwargs={"pk": 0}), {})
        self.assertEqual(response.status_code, 404)

    def test_patch_invalid(self):
        """400"""

        o = UserFactory.create()

        self.authenticate()
        response = self.client.patch(
            reverse("users:detail", kwargs={"pk": o.id}), {"is_active": "test"})
        self.assertEqual(response.status_code, 400)

    def test_patch_ok(self):
        """200"""

        o = UserFactory.create(is_active=False)

        self.authenticate()
        response = self.client.patch(
            reverse("users:detail", kwargs={"pk": o.id}), {"is_active": True})
        self.assertEqual(response.status_code, 200)

    def test_put_unauthenticated(self):
        """401"""

        response = self.client.put(
            reverse("users:detail", kwargs={"pk": 0}), {})
        self.assertEqual(response.status_code, 401)

    def test_put_object_does_not_exist(self):
        """404"""

        self.authenticate()
        response = self.client.put(
            reverse("users:detail", kwargs={"pk": 0}), {})
        self.assertEqual(response.status_code, 404)

    def test_put_invalid(self):
        """400"""

        o = UserFactory.create()
        payload = model_to_dict(o)
        payload["is_active"] = "test"

        self.authenticate()
        response = self.client.put(
            reverse("users:detail", kwargs={"pk": o.id}), payload)
        self.assertEqual(response.status_code, 400)

    def test_put_ok(self):
        """200"""

        o = UserFactory.create(is_active=True)
        payload = model_to_dict(o)
        payload["is_active"] = False

        self.authenticate()
        response = self.client.put(
            reverse("users:detail", kwargs={"pk": o.id}), payload)
        self.assertEqual(response.status_code, 200)


class UserListTest(BaseAPITestCase):
    """
    Tests the 'users:list' endpoint.
    """

    def test_get_unauthenticated(self):
        """401"""

        response = self.client.get(reverse("users:list"))
        self.assertEqual(response.status_code, 401)

    def test_get_ok(self):
        """200"""

        self.authenticate()
        response = self.client.get(reverse("users:list"))
        self.assertEqual(response.status_code, 200)

    def test_post_unauthenticated(self):
        """401"""

        response = self.client.post(reverse("users:list"), {})
        self.assertEqual(response.status_code, 401)

    def test_post_invalid(self):
        """400"""

        self.authenticate()
        response = self.client.post(reverse("users:list"), {})
        self.assertEqual(response.status_code, 400)

    def test_post_ok(self):
        """201"""

        payload = UserFactory.attributes()

        self.authenticate()
        response = self.client.post(reverse("users:list"), payload)
        self.assertEqual(response.status_code, 201)
