from .models import Teacher
from django.contrib import admin


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'department', 'is_active')
    list_filter = ('department', 'subjects', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('id',)
    filter_horizontal = ('subjects',)
