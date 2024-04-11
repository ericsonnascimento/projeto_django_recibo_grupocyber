from django import forms
from . import models
from django.forms.widgets import TextInput
from django.utils.safestring import mark_safe

class PhoneMaskWidget(TextInput):
    def __init__(self, attrs=None):
        default_attrs = {
            'class': 'form-control', 
            'placeholder': 'Ex.: (81)98888-8888'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)

    def render(self, name, value, attrs=None, renderer=None):
        rendered = super().render(name, value, attrs, renderer)
        return rendered + mark_safe(
            """
            <script>
                document.addEventListener('DOMContentLoaded', function() {
                    Inputmask('(99)99999-9999').mask('#id_%s');
                });
            </script>
            """ % name
        )

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
            'phone': PhoneMaskWidget(),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: severinosilva@gmail.com'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name:
            return name.upper()
        return name