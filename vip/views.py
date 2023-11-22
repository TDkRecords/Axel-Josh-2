from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Vip
from django.contrib.auth.models import Group

@login_required
def vip(request):
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
    vip_dict = Vip.objects.all()
    return render(request, 'vip.html', {'vip_dict': vip_dict, 'num_usuarios_en_grupo': num_usuarios_en_grupo})

def exit(request):
    logout(request)
    return redirect('home')