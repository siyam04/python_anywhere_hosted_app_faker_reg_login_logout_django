from django.contrib import admin
# Same App importing
from fourth_app_reg_login_logout.models import UserProfileInfo


class UserProfileInfoAdmin(admin.ModelAdmin):
    """ Customizing Fields for UserProfileInfo Class """
    list_display = ['id', 'user', 'portfolio_site', 'profile_pic']
    list_display_links = ['user']
    list_filter = ['user']
    search_fields = ['user']


# Registering All Classes
admin.site.register(UserProfileInfo, UserProfileInfoAdmin)
