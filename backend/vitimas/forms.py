from django import forms
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['cpf', 'nome', 'email', 'senha', 'telefone',
                  'data_nascimento', 'cep', 'bairro', 'numero', 'complemento']
