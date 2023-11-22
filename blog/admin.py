from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'date_post']
    ordering = ['-date_post']  # Esto ordenará las publicaciones por fecha de publicación de forma descendente