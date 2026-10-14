from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Inclui as URLs da app core
    path('', lambda request: redirect('listar_projetos')),  # Redireciona a página inicial diretamente para a lista de projetos
]