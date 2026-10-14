from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Projeto, Tarefa
from .forms import ProjetoForm, TarefaForm

# ================= VIEWS DE PROJETOS =================

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

# ================= VIEWS DE TAREFAS =================

def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'core/listar_tarefas.html', {'tarefas': tarefas})

def criar_tarefa(request):
    form = TarefaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Tarefa criada com sucesso!')
        return redirect('listar_tarefas')
    return render(request, 'core/form_tarefa.html', {'form': form, 'titulo': 'Nova Tarefa'})

def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    form = TarefaForm(request.POST or None, instance=tarefa)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Tarefa atualizada com sucesso!')
        return redirect('listar_tarefas')
    return render(request, 'core/form_tarefa.html', {'form': form, 'titulo': 'Editar Tarefa'})

def eliminar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa eliminada com sucesso!')
        return redirect('listar_tarefas')
    return render(request, 'core/confirmar_eliminar_tarefa.html', {'tarefa': tarefa})