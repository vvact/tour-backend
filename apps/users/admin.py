from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
            'fields': (
                'first_name', 'last_name', 'email', 'phone_number',
                'profile_picture', 'bio'
            )
        }),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    list_display = (
        'uuid',          # <-- Added UUID
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('uuid', 'username', 'email', 'first_name', 'last_name')  # <-- Added uuid
    ordering = ('-date_joined',)
    readonly_fields = ('uuid',)  # <-- Make UUID read-only in detail view