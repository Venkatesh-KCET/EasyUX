from django.contrib import admin
from .models import Config, Organization
from unfold.admin import ModelAdmin

@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ('config_name', 'organization', 'config_value')
    search_fields = ('config_name', 'organization__name')
    list_filter = ('organization',)

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