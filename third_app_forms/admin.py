from django.contrib import admin
# Same App importing
from third_app_forms.models import User


class UserAdmin(admin.ModelAdmin):
    """ Customizing Fields for User Class """
    list_display = ['id', 'username', 'first_name', 'last_name', 'email', 'verify_email']
    list_display_links = ['username']
    list_filter = ['username', 'email']
    search_fields = ['username', 'email']


# Registering All Classes
admin.site.register(User, UserAdmin)