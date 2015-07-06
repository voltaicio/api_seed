from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        fields = (
            "date_joined", "email", "id", "is_active", "is_staff",
            "is_superuser", "last_login")
        model = User
        read_only_fields = ("date_joined", "id", "last_login")
