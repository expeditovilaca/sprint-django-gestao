from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Projeto
from .forms import ProjetoForm

def listar_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'core/listar_projetos.html', {'projetos': projetos})

def criar_projeto(request):
    form = ProjetoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Projeto criado com sucesso!')
        return redirect('listar_projetos')
    return render(request, 'core/form_projeto.html', {'form': form, 'titulo': 'Novo Projeto'})

def editar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    form = ProjetoForm(request.POST or None, instance=projeto)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Projeto atualizado com sucesso!')
        return redirect('listar_projetos')
    return render(request, 'core/form_projeto.html', {'form': form, 'titulo': 'Editar Projeto'})

def eliminar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        projeto.delete()
        messages.success(request, 'Projeto eliminado com sucesso!')
        return redirect('listar_projetos')
    return render(request, 'core/confirmar_eliminar_projeto.html', {'projeto': projeto})