from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'grade', 'group', 'email', 'phone_number', 'parent_name', 'parent_phone')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number', 'parent_name', 'parent_phone')
    list_filter = ('grade', 'gender', 'group')
    ordering = ('last_name', 'first_name')
