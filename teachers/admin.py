from django.contrib import admin
from import_export.admin import ExportMixin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'department', 'employment_type', 'join_date', 'is_active')
    search_fields = ('first_name', 'last_name', 'email', 'phone', 'department__name')
    list_filter = ('employment_type', 'department', 'is_active', 'join_date')
    ordering = ('last_name', 'first_name')
    filter_horizontal = ('subjects',)
    list_editable = ('is_active',)
    list_per_page = 20
    date_hierarchy = 'join_date'
    readonly_fields = ('join_date',)
