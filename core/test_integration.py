from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict

from .factories import ThingFactory
from utils.testing import BaseAPITestCase


class ThingDetailTest(BaseAPITestCase):
    """
    """

    def test_delete_unauthenticated(self):
        """401"""

        response = self.client.delete(reverse("core:thing_detail", kwargs={"pk": 0}))
        self.assertEqual(response.status_code, 401)

    def test_delete_object_does_not_exist(self):
        """404"""

        self.authenticate()
        response = self.client.delete(reverse("core:thing_detail", kwargs={"pk": 0}))
        self.assertEqual(response.status_code, 404)

    def test_delete_ok(self):
        """204"""

        o = ThingFactory.create()

        self.authenticate()
        response = self.client.delete(
            reverse("core:thing_detail", kwargs={"pk": o.id}))
        self.assertEqual(response.status_code, 204)

    def test_get_unauthenticated(self):
        """401"""

        response = self.client.get(reverse("core:thing_detail", kwargs={"pk": 0}))
        self.assertEqual(response.status_code, 401)

    def test_get_object_does_not_exist(self):
        """404"""

        self.authenticate()
        response = self.client.get(reverse("core:thing_detail", kwargs={"pk": 0}))
        self.assertEqual(response.status_code, 404)

    def test_get_ok(self):
        """200"""

        o = ThingFactory.create()

        self.authenticate()
        response = self.client.get(reverse("core:thing_detail", kwargs={"pk": o.id}))
        self.assertEqual(response.status_code, 200)

    def test_patch_unauthenticated(self):
        """401"""

        response = self.client.patch(reverse("core:thing_detail", kwargs={"pk": 0}))
        self.assertEqual(response.status_code, 401)

    def test_patch_invalid(self):
        """400"""

        o = ThingFactory.create()
        payload = {"name": ""}

        self.authenticate()
        response = self.client.patch(
            reverse("core:thing_detail", kwargs={"pk": o.id}), payload)
        self.assertEqual(response.status_code, 400)

    def test_patch_ok(self):
        """200"""

        o = ThingFactory.create()
        payload = {"name": "test"}

        self.authenticate()
        response = self.client.patch(
            reverse("core:thing_detail", kwargs={"pk": o.id}), payload)
        self.assertEqual(response.status_code, 200)

    def test_put_unauthenticated(self):
        """401"""

        response = self.client.put(reverse("core:thing_detail", kwargs={"pk": 0}))
        self.assertEqual(response.status_code, 401)

    def test_put_invalid(self):
        """400"""

        o = ThingFactory.create()

        self.authenticate()
        response = self.client.put(
            reverse("core:thing_detail", kwargs={"pk": o.id}), {})
        self.assertEqual(response.status_code, 400)

    def test_put_ok(self):
        """200"""

        o = ThingFactory.create()
        payload = model_to_dict(o)
        payload["name"] = "test"

        self.authenticate()
        response = self.client.put(
            reverse("core:thing_detail", kwargs={"pk": o.id}), payload)
        self.assertEqual(response.status_code, 200)


class ThingListTest(BaseAPITestCase):
    """
    """

    def test_get_unauthenticated(self):
        """401"""

        response = self.client.get(reverse("core:thing_list"))
        self.assertEqual(response.status_code, 401)

    def test_get_ok(self):
        """200"""

        self.authenticate()
        response = self.client.get(reverse("core:thing_list"))
        self.assertEqual(response.status_code, 200)

    def test_post_unauthenticated(self):
        """401"""

        response = self.client.post(reverse("core:thing_list"))
        self.assertEqual(response.status_code, 401)

    def test_post_invalid(self):
        """400"""

        self.authenticate()
        response = self.client.post(reverse("core:thing_list"), {})
        self.assertEqual(response.status_code, 400)

    def test_post_ok(self):
        """201"""

        payload = ThingFactory.attributes()

        self.authenticate()
        response = self.client.post(reverse("core:thing_list"), payload)
        self.assertEqual(response.status_code, 201)
