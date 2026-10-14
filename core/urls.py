from django.urls import path
from . import views

urlpatterns = [
    # Rotas de Projetos
    path('projetos/', views.listar_projetos, name='listar_projetos'),
    path('projetos/novo/', views.criar_projeto, name='criar_projeto'),
    path('projetos/<int:pk>/editar/', views.editar_projeto, name='editar_projeto'),
    path('projetos/<int:pk>/eliminar/', views.eliminar_projeto, name='eliminar_projeto'),

    # Rotas de Tarefas
    path('tarefas/', views.listar_tarefas, name='listar_tarefas'),
    path('tarefas/nova/', views.criar_tarefa, name='criar_tarefa'),
    path('tarefas/<int:pk>/editar/', views.editar_tarefa, name='editar_tarefa'),
    path('tarefas/<int:pk>/eliminar/', views.eliminar_tarefa, name='eliminar_tarefa'),
]