from django.shortcuts import render
from django.contrib.auth.models import Group
from .models import Project

def home(request):
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
    projects = Project.objects.all()

    # Agrega la variable num_usuarios_en_grupo al contexto
    return render(request, 'home.html', {'projects': projects, 'num_usuarios_en_grupo': num_usuarios_en_grupo})
