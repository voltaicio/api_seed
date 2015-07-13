from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import Creatable, Modifiable


class Thing(Creatable, Modifiable):
    """
    """

    name = models.CharField(_("name"), max_length=128)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
