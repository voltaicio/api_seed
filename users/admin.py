from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    """
    An admin for app users.
    """

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2",)
        })
    )
    add_form = UserCreationForm
    form = UserChangeForm
    fieldsets = (
        (None, {"fields": (
            "email", "password", "date_joined",)}),
        ("Permissions", {"fields": (
            "is_active", "is_staff", "is_superuser",)}),
    )
    filter_horizontal = ()
    list_display = (
        "id", "email", "is_active", "is_staff", "is_superuser", "date_joined",)
    list_filter = ("is_active", "is_staff", "is_superuser",)
    ordering = ("id", "email",)
    search_fields = ("email",)


admin.site.register(User, UserAdmin)
