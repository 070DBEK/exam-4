from django.contrib import admin
from .models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'credit_hours', 'grade_level', 'prerequisites']
    list_filter = ['department', 'grade_level']
    search_fields = ['name', 'prerequisites']
