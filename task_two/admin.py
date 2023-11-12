from django.contrib import admin

from task_two.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "home_city")
