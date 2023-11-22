from django.contrib import admin
from .models import Vip

@admin.register(Vip)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'image','files', 'instructions', 'date_vip']
    ordering = ['-date_vip']  # Esto ordenará las publicaciones por fecha de publicación de forma descendente