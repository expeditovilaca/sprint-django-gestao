from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Tarefa
from .forms import TarefaForm

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().select_related('projeto')
    return render(request, 'core/listar_tarefas.html', {'tarefas': tarefas})


def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa criada com sucesso!')
            return redirect('listar_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'core/form.html', {'form': form, 'titulo_pagina': 'Nova Tarefa'})


def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('listar_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'core/form_tarefa.html', {'form': form, 'titulo_pagina': 'Editar Tarefa'})

# Excluir Tarefa
def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('listar_tarefas')
    return render(request, 'core/confirmar.html', {'tarefa': tarefa})
