from django.contrib import admin
from .models import Task, CadastroAnimais, RegistroClinico

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'completed', 'user')
    list_filter = ('completed', 'user')
    search_fields = ('title', 'description')

@admin.register(CadastroAnimais)
class CadastroAnimaisAdmin(admin.ModelAdmin):
    list_display = ('especie', 'nome', 'idade', 'nome_proprietario', 'raca', 'caracteristicas')
    search_fields = ('especie', 'nome', 'nome_proprietario', 'raca', 'caracteristicas')

@admin.register(RegistroClinico)
class RegistroClinicoAdmin(admin.ModelAdmin):
    list_display = ('animal', 'data_consulta', 'diagnostico', 'prescricao', 'observacoes')
    list_filter = ('data_consulta', 'animal')
    search_fields = ('diagnostico', 'prescricao', 'observacoes')

