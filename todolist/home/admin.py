from django.contrib import admin

# Register your models here.
from home.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'address', 'city', 'country']

admin.site.register(UserProfile,UserProfileAdmin)
