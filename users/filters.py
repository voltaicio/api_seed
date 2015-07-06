from django.contrib.auth import get_user_model

import django_filters

User = get_user_model()


class UserFilter(django_filters.FilterSet):
    """
    """

    class Meta:
        fields = ["date_joined", "email", "is_active", "is_staff", "last_login"]
        model = User
        search_fields = ["email"]
