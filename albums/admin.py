from django.contrib import admin
from .models import canciones

@admin.register(canciones)
class PostAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'pista', 'date_singles']
    ordering = ['-date_singles']  # Esto ordenará las publicaciones por fecha de publicación de forma descendente