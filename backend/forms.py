from datetime import datetime
from django import forms
from django.forms import fields
from .models import Historico
import os

scripts = (
    ('docker_compose.py', 'Docker Compose'),
    ('down.py', 'Docker Compose Down'),
    ('restart.py','Restart Mysql')
    # ('list.py', 'Lista')

)

class SalvarHistorico(forms.ModelForm): #RunForm
    class Meta:
        model = Historico
        fields= ("servidor","script")

class HistoricoForms(forms.Form):
    servidor = forms.CharField(max_length=50,  widget=forms.TextInput(attrs={'placeholder': 'Selecione o servidor'}), label='Servidor')
    usuario= forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Usuário do servidor'}), label='Usuário')
    senha= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha do servidor'}))
    script = forms.ChoiceField(choices=scripts)
    error = forms.CharField(widget=forms.HiddenInput()) 
    data = forms.DateTimeField(widget=forms.HiddenInput())
    terminal = forms.CharField(widget=forms.HiddenInput()) 