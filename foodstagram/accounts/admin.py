from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import FoodstagramUserCreationForm, FoodstagramUserChangeForm

UserModel = get_user_model()


@admin.register(UserModel)
class FoodstagramUserAdmin(UserAdmin):
    add_form = FoodstagramUserCreationForm
    form = FoodstagramUserChangeForm

    list_display = ('pk', 'email', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    ordering = ('pk',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:  # For adding new user
            return self.add_fieldsets
        if request.user.is_superuser:  # Only superusers can modify is_superuser field
            return (
                (None, {'fields': ('email', 'password')}),
                ('Personal info', {'fields': ()}),
                ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
                ('Important dates', {'fields': ('last_login',)}),
            )
        return super().get_fieldsets(request, obj)

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return self.readonly_fields + ('is_superuser',)
        return self.readonly_fields
