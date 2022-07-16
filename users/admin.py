import django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    list_display = ("username", "corpname", "email")

    fieldsets = UserAdmin.fieldsets + (("회사명", {"fields": ("corpname",)}),)
