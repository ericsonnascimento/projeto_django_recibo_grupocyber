from django import forms
from . import models
from django.forms.widgets import TextInput
from django.utils.safestring import mark_safe

class PriceMaskWidget(TextInput):
    def __init__(self, attrs=None):
        default_attrs = {
            'class': 'form-control', 
            'placeholder': 'Ex.: R$ 1000,00'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)

    def render(self, name, value, attrs=None, renderer=None):
        rendered = super().render(name, value, attrs, renderer)
        return rendered + mark_safe(
            """
            <script>
                document.addEventListener('DOMContentLoaded', function() {
                    Inputmask('9{+},99').mask('#id_%s');
                });
            </script>
            """ % name
        )

class ReceiptsForms(forms.ModelForm):
    class Meta:
        model = models.Receipts
        exclude = ['user']
        labels = {
            'client': 'Cliente',
            'price': 'Valor R$:',
            'text': 'Correspondente a:',
        }

        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'price': PriceMaskWidget(),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
        }
