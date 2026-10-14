from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_inicio = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    PRIORIDADE_CHOICES = [
        ('BAIXA', 'Baixa'),
        ('MEDIA', 'Média'),
        ('ALTA', 'Alta'),
    ]

    titulo = models.CharField(max_length=200, verbose_name="Título")
    prioridade = models.CharField(
        max_length=10, 
        choices=PRIORIDADE_CHOICES, 
        default='MEDIA', 
        verbose_name="Prioridade"
    )
    concluido = models.BooleanField(default=False, verbose_name="Concluído")
    projeto = models.ForeignKey(
        Projeto, 
        on_delete=models.CASCADE, 
        related_name='tarefas', 
        verbose_name="Projeto"
    )

    def __str__(self):
        return f"{self.titulo} - {self.projeto.nome}"