from django.contrib import admin
from import_export.admin import ExportMixin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'department', 'employment_type', 'join_date', 'is_active')
    search_fields = ('first_name', 'last_name', 'email', 'phone', 'department__name')
    list_filter = ('employment_type', 'department', 'is_active', 'join_date')
    ordering = ('last_name', 'first_name')
    filter_horizontal = ('subjects',)  # ManyToManyField uchun yaxshiroq UI
    list_editable = ('is_active',)  # Admin sahifasidan bevosita statusni o‘zgartirish
    list_per_page = 20  # Har bir sahifada 20 ta ma’lumot chiqarish
    date_hierarchy = 'join_date'  # Sanalar bo‘yicha saralash
    readonly_fields = ('join_date',)  # Ishga kirgan sanani faqat ko‘rish mumkin
