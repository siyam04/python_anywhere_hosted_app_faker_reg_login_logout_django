from django.contrib import admin
# Same App importing
from .models import User


class UserAdmin(admin.ModelAdmin):
    """ Customizing Fields for User Class """
    list_display = ['id', 'first_name', 'last_name', 'email']
    list_filter = ['email']
    search_fields = ['email', 'first_name', 'last_name']


# Registering All Classes
admin.site.register(User, UserAdmin)