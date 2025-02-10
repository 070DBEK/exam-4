from django.contrib import admin
from .models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade_level', 'class_teacher', 'schedule', 'academic_year', 'max_students')
    search_fields = ('name', 'academic_year', 'class_teacher__last_name', 'class_teacher__first_name')
    list_filter = ('grade_level', 'schedule', 'academic_year')
    ordering = ('grade_level', 'name')
    filter_horizontal = ('subjects', 'students')

