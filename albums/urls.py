from django.urls import path
from .views import musica_render

app_name = 'albums'

urlpatterns = [
    path('', musica_render, name="musica"),
]
