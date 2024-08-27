from django import forms
from .models import CadastroAnimais, RegistroClinico

class CadastroAnimaisForm(forms.ModelForm):
    class Meta:
        model = CadastroAnimais
        fields = ['especie', 'nome', 'idade', 'nome_proprietario', 'raca', 'caracteristicas']

class RegistroClinicoForm(forms.ModelForm):
    class Meta:
        model = RegistroClinico
        fields = ['animal', 'data_consulta', 'diagnostico', 'prescricao', 'observacoes']