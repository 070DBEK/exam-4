from django.contrib import admin
from .models import Director


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'birth', 'bio', 'picture')
    search_fields = ('last_name', 'first_name')
    list_filter = ('birth',)
    ordering = ('last_name', 'first_name')
