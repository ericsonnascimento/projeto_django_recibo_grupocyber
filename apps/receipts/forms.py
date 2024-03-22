from django import forms
from . import models

class ReceiptsForms(forms.ModelForm):
    class Meta:
        model = models.Receipts
        exclude = ['user']
        labels = {
            'client': 'Cliente',
            'price': 'Valor R$',
            'text': 'Correspondente a:',
        }

        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
        }
