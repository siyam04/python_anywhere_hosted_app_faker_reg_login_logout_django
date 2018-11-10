from django.contrib import admin
# Same app importing
from app_CBV_Mixins.models import School, Student


class SchoolAdmin(admin.ModelAdmin):
    """Customizing Fields for School Class"""
    list_display = ['id', 'name', 'principal', 'location']
    list_display_links = ['name']
    list_filter = ['name', 'location']
    search_fields = ['name']


class StudentAdmin(admin.ModelAdmin):
    """Customizing Fields for Student Class"""
    list_display = ['id', 'name', 'age', 'school']
    list_display_links = ['name']
    list_filter = ['name', 'school']
    search_fields = ['name']


admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)
