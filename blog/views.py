from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import Group

def render_posts(request):
    # Obtén el grupo específico
    nombre_del_grupo = 'Acceso_Vip'  # Reemplaza con el nombre real del grupo
    try:
        grupo = Group.objects.get(name=nombre_del_grupo)
    except Group.DoesNotExist:
        grupo = None

    # Inicializa el número de usuarios en el grupo
    num_usuarios_en_grupo = 0

    # Si el grupo existe, obtén el número de usuarios en ese grupo
    if grupo:
        num_usuarios_en_grupo = grupo.user_set.count() # type: ignore

    # Obtén todos los proyectos
    posts = Post.objects.all()

    # Agrega la variable num_usuarios_en_grupo al contexto
    return render(request, 'posts.html', {'posts': posts, 'num_usuarios_en_grupo': num_usuarios_en_grupo})

def post_detail(request, post_id):
    # Obtén el grupo específico
    nombre_del_grupo = 'Acceso_Vip'  # Reemplaza con el nombre real del grupo
    try:
        grupo = Group.objects.get(name=nombre_del_grupo)
    except Group.DoesNotExist:
        grupo = None

    # Inicializa el número de usuarios en el grupo
    num_usuarios_en_grupo = 0

    # Si el grupo existe, obtén el número de usuarios en ese grupo
    if grupo:
        num_usuarios_en_grupo = grupo.user_set.count() # type: ignore

    # Agrega la variable num_usuarios_en_grupo al contexto
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post, 'num_usuarios_en_grupo': num_usuarios_en_grupo})