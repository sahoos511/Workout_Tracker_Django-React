from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    readonly_fields = ('date_joined',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )