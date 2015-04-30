from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.fields import AutoCreatedField, AutoLastModifiedField


class AbstractCreated(models.Model):
    """
    """

    created = AutoCreatedField(_("created"))

    class Meta:
        abstract = True


class AbstractModified(models.Model):
    """
    """

    modified = AutoLastModifiedField(_("modified"))

    class Meta:
        abstract = True


class AbstractCreatedModified(AbstractCreated, AbstractModified):
    """
    """

    class Meta:
        abstract = True
