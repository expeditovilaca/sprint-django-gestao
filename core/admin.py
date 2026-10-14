from django.contrib import admin

from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'projeto', 'prioridade', 'concluido')
    list_filter = ('prioridade', 'concluido', 'projeto')
    search_fields = ('titulo',)
