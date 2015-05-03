from django.contrib import admin

from .models import Thing


class ThingAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": ("name",)
        }),
        ("Meta", {
            "classes": ("grp-collapse grp-closed",),
            "fields": ("created", "id", "modified",)
        })
    )
    list_display = ("id", "name", "created", "modified",)
    readonly_fields = ("created", "id", "modified",)
    search_fields = ("name",)


admin.site.register(Thing, ThingAdmin)
