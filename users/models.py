from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """
    A model manager for User.
    """

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """

        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """

        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """
    A model for app users.

    @see https://docs.djangoproject.com/en/1.8/topics/auth/customizing/#a-full-example
    """

    date_joined = models.DateTimeField(
        _("date joined"),
        default=timezone.now)
    email = models.EmailField(
        _("email address"),
        max_length=128,
        unique=True)
    is_active = models.BooleanField(
        _("is active"),
        default=True)
    is_staff = models.BooleanField(
        _("is staff"),
        default=False)
    is_superuser = models.BooleanField(
        _("is superuser"),
        default=False)

    objects = UserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email
