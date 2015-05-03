import factory

from .models import Thing


class ThingFactory(factory.DjangoModelFactory):
    """
    """

    name = factory.Sequence(lambda n: "name-{0}".format(n))

    class Meta:
        model = Thing
