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

class UserEditForm(forms.Form):
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

    def clean_login_registration(self):
        login_user = self.cleaned_data.get('login_registration')

        if login_user:
            login_user = login_user.strip()
            if ' ' in login_user:
                raise forms.ValidationError('Não é permitido espaços no campo "Login"') 
                
        return login_user

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

    def clean_login_registration(self):
        login_user = self.cleaned_data.get('login_registration')
        if login_user:
            login_user = login_user.strip()
            if ' ' in login_user:
                raise forms.ValidationError('Não é permitido espaços no campo "Login"')
        return login_user

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')

        if password != password_repeat:
            raise forms.ValidationError('Senha digitada no campo "Senha" e "Repita a senha" são diferentes!')
        if len(password) < 8:
            raise forms.ValidationError('Senha deve conter pelo menos 8 caracteres')
        if not re.search("[A-Z]", password):
            raise forms.ValidationError('A senha deve conter pelo menos uma letra maiúscula')
        if not re.search("[a-z]", password):
            raise forms.ValidationError('A senha deve conter pelo menos uma letra minúscula')
        if not re.search("[0-9]", password):
            raise forms.ValidationError('A senha deve conter pelo menos um número')
        if not re.search("[@#$%^&+=]", password):
            raise forms.ValidationError('A senha deve conter pelo menos um caractere especial')
        return password