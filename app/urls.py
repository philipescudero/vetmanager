from django.urls import path
from .views import cadastro_animais, registro_animais, visualizar_registros

urlpatterns = [
    path('cadastro/', cadastro_animais, name='cadastro_animais'),
    path('registro/', registro_animais, name='registro_animais'),
    path('visualizar_registros/', visualizar_registros, name='visualizar_registros'),
]
