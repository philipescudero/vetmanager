from django.shortcuts import render, redirect
from django.views.generic import ListView  # Importando ListView
from .models import CadastroAnimais, RegistroClinico
from .forms import CadastroAnimaisForm, RegistroClinicoForm

def cadastro_animais(request):
    if request.method == 'POST':
        form = CadastroAnimaisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redireciona após o cadastro
    else:
        form = CadastroAnimaisForm()
    return render(request, 'cadastro.html', {'form': form})

def registro_animais(request):
    if request.method == 'POST':
        form = RegistroClinicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirecione para uma página de sucesso ou a página inicial
    else:
        form = RegistroClinicoForm()
    return render(request, 'registro_animais.html', {'form': form})

def visualizar_registros(request):
    registros = RegistroClinico.objects.all()  # Obtém todos os registros de consultas
    return render(request, 'visualizar_registros.html', {'registros': registros})