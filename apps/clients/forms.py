from django import forms
from . import models

class ClientRegisterForms(forms.ModelForm):
    class Meta:
        model = models.Client_Register
        exclude = []
        labels = {
            'name': 'Nome',
            'phone': 'Telefone',
            'email': 'Email',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Severino da Silva'}),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: (81)98888-8888'}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: severinosilva@gmail.com'}),
        }