from django.contrib.auth import get_user_model

import factory
from factory import fuzzy

User = get_user_model()


class UserFactory(factory.DjangoModelFactory):
    email = factory.Sequence(lambda n: "factory-email-{0}@test.com".format(n))
    is_active = fuzzy.FuzzyChoice([True, False])
    is_staff = fuzzy.FuzzyChoice([True, False])
    is_superuser = fuzzy.FuzzyChoice([True, False])

    class Meta:
        model = User

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = "adm1n"
        if "password" in kwargs:
            password = kwargs.pop("password")

        user = super(UserFactory, cls)._prepare(create, **kwargs)
        user.set_password(password)

        if create:
            user.save()

        return user
