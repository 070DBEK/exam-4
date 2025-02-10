from django.contrib import admin
from .models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'grade_level', 'credit_hours', 'prerequisites')
    search_fields = ('name', 'department__name')
    list_filter = ('grade_level', 'department')
    ordering = ('name',)
