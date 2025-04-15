# authentication/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Organization

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('organization',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('organization',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'updated_at', 'created_by', 'updated_by')
    search_fields = ('name', 'address', 'phone_number')
    list_filter = ('is_active', 'created_at')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'is_active', 'logo', 'address', 'phone_number', 'website')
        }),
        ('Tracking Info', {
            'fields': ('created_by', 'updated_by', 'created_at', 'updated_at')
        }),
    )