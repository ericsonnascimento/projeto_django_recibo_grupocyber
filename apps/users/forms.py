from django import forms
import re

class LoginForms(forms.Form):
    login_name = forms.CharField(
        label='Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu login'
            }
        )
    )

    login_password = forms.CharField(
        label='Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )


class UserRegistrationForm(forms.Form):
    name_registration = forms.CharField(
        label='Nome',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome completo'
            }
        )
    )

    login_registration = forms.CharField(
        label='Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva'
            }
        )
    )

    password = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite uma senha'
            }
        )
    )

    password_repeat = forms.CharField(
        label='Repita a senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a senha novamente'
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        login_user = cleaned_data.get('login_registration')
        senha_1 = cleaned_data.get('password')
        senha_2 = cleaned_data.get('password_repeat')

        if login_user:
            login_user = login_user.strip()
            if ' ' in login_user:
                raise forms.ValidationError('Não é permitido espaços no campo "Login"')

        if len(senha_1) < 8:
            raise forms.ValidationError('Senha deve contar pelo menos 8 caracteres')
        
        if not re.search("[A-Z]", senha_1):
            raise forms.ValidationError('A senha deve conter pelo menos uma letra maiúscula')

        if not re.search("[a-z]", senha_1):
            raise forms.ValidationError('A senha deve conter pelo menos uma letra minúscula')

        if not re.search("[0-9]", senha_1):
            raise forms.ValidationError('A senha deve conter pelo menos um número')

        if not re.search("[@#$%^&+=]", senha_1):
            raise forms.ValidationError('A senha deve conter pelo menos um caractere especial')
        
        if senha_1 and senha_2 and senha_1 != senha_2:
            raise forms.ValidationError('Senhas digitadas não são iguais!')  
        
        return cleaned_data

