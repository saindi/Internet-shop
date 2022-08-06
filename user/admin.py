from django.contrib import admin
from user.models import UserModel


class UserModelAdmin(admin.ModelAdmin):
    list_display = "username", "first_name", "last_name"


admin.site.register(UserModel, UserModelAdmin)