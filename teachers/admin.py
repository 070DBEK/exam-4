from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'department', 'employment_type', 'join_date', 'is_active')
    search_fields = ('first_name', 'last_name', 'email', 'phone', 'department__name')
    list_filter = ('employment_type', 'department', 'is_active')
    ordering = ('last_name', 'first_name')
    filter_horizontal = ('subjects',)
