from django.contrib import admin
from .models import Project

@admin.register(Project)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'url', 'date_portfolio']
    ordering = ['-date_portfolio']  # Esto ordenará las publicaciones por fecha de publicación de forma descendente