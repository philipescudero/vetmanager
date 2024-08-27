from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    completed = models.BooleanField(default=False, verbose_name='Concluído')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'

    def __str__(self):
        return self.title


class CadastroAnimais(models.Model):
    ESPECIES_CHOICES = [
        ('Gato', 'Gato'),
        ('Cachorro', 'Cachorro'),
        ('Pássaro', 'Pássaro'),
        ('Peixe', 'Peixe'),
        ('Coelho', 'Coelho'),
        ('Hamster', 'Hamster'),
        ('Réptil', 'Réptil'),
        ('Cavalo', 'Cavalo'),
        ('Porquinho da Índia', 'Porquinho da Índia'),
        ('Outro', 'Outro'),
    ]
    
    nome = models.CharField(max_length=100, verbose_name='Nome do animal')
    idade = models.IntegerField(verbose_name='Idade do animal')
    nome_proprietario = models.CharField(max_length=100, verbose_name='Nome do proprietário')
    raca = models.CharField(max_length=100, verbose_name='Raça', default='Raça não informada')
    caracteristicas = models.TextField(verbose_name='Características Distintivas', blank=True, null=True)
    especie = models.CharField(max_length=50, choices=ESPECIES_CHOICES, verbose_name='Espécie do animal', default='Outro')

    def __str__(self):
        return f'{self.nome} ({self.especie}) - Proprietário: {self.nome_proprietario}'

class RegistroClinico(models.Model):
    animal = models.ForeignKey(CadastroAnimais, on_delete=models.CASCADE, verbose_name='Animal', null=True, blank=True)
    data_consulta = models.DateField(verbose_name='Data da consulta')
    diagnostico = models.TextField(verbose_name='Diagnóstico do animal')
    prescricao = models.TextField(verbose_name='Prescrição médica')
    observacoes = models.CharField(max_length=100, verbose_name='Observações', null=True, blank=True)

    def __str__(self):
        return f'{self.data_consulta} - Diagnóstico ({self.diagnostico}) - Prescrição médica'
    
