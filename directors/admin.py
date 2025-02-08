from django.contrib import admin
from .models import Director

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'birth')
    search_fields = ('last_name', 'first_name')