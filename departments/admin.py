from django.contrib import admin
from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head', 'location', 'contact_email', 'contact_phone')
    search_fields = ('name', 'location', 'contact_email')
    list_filter = ('location',)
    ordering = ('name',)
