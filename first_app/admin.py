from django.contrib import admin
# Same App importing
from .models import (
    Topic,
    WebPage,
    AccessRecord,
)


class TopicAdmin(admin.ModelAdmin):
    """ Customizing Fields for Topic Class """
    list_display = [ 'id', 'top_name']
    list_display_links = ['top_name']
    list_filter = ['top_name']
    search_fields = ['top_name']
    # prepopulated_fields = {'slug': ('title',)}


class WebPageAdmin(admin.ModelAdmin):
    """ Customizing Fields for WebPage Class """
    list_display = ['id', 'name', 'topic', 'url']
    list_display_links = ['name']
    list_filter = ['topic', 'name']
    list_editable = ['topic']
    search_fields = ['topic', 'name']


class AccessRecordAdmin(admin.ModelAdmin):
    """ Customizing Fields for AccessRecord Class """
    list_display = ['id', 'name', 'date']
    list_display_links = ['name']
    list_filter = ['date', 'name']
    list_editable = ['date']
    search_fields = ['name']


# Registering All Classes
admin.site.register(Topic, TopicAdmin)
admin.site.register(WebPage, WebPageAdmin)
admin.site.register(AccessRecord, AccessRecordAdmin)
