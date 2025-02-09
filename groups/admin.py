from django.contrib import admin
from .models import Group

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade_level', 'class_teacher', 'schedule', 'academic_year', 'max_students')
    list_filter = ('grade_level', 'schedule', 'academic_year')
    search_fields = ('name', 'class_teacher__first_name', 'class_teacher__last_name')
    filter_horizontal = ('subjects', 'students')
