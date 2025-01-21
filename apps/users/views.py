from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import auth, messages
from . import forms

def login(request):
    form = forms.LoginForms()

    if request.method == 'POST':
        form = forms.LoginForms(request.POST)

        if form.is_valid():
            login_name = form['login_name'].value()
            login_password = form['login_password'].value()


        usuario = auth.authenticate(
            username=login_name,
            password=login_password,
        )

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'Bem vindo {usuario}, credenciais aceitas com sucesso!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuário ou senha inválidos')

    return render(request, 'users/login.html', {'form': form})


def user_register(request):
    if not request.user.is_authenticated:
        return redirect('login')

    form = forms.UserRegistrationForm()

    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)

        if form.is_valid():
            name_registration = form['name_registration'].value()
            login_registration = form['login_registration'].value()
            password_registration = form['password'].value()
        
            if User.objects.filter(username=login_registration).exists():
                messages.error(request, f'Usuário "{login_registration}" já existe, tente um novo usuário!')
            
            else:
                user = User.objects.create_user(
                    username=login_registration,
                    first_name=name_registration,
                    password=password_registration
                )
                messages.success(request, 'Usuário cadastrado com sucesso!')
                return redirect('user_list')
            
    return render(request, 'users/user_register.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Volte sempre!')
    return redirect('login')

def user_list(request):
    if not request.user.is_authenticated:
        return redirect('login')

    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

def user_edit(request, id_user):
    if not request.user.is_authenticated:
        return redirect('login')

    user_instance = get_object_or_404(User, id=id_user)

    if request.method == 'POST':
        form = forms.UserEditForm(request.POST)
        if form.is_valid():
            user_instance.first_name = form.cleaned_data['name_registration']
            user_instance.username = form.cleaned_data['login_registration']
            user_instance.save()
            messages.success(request, 'Usuário alterado com sucesso!')
            return redirect('user_list')
    else:
        form = forms.UserEditForm(initial={
            'name_registration': user_instance.first_name,
            'login_registration': user_instance.username,
        })

    return render(request, 'users/user_edit.html', {'form': form, 'id_user': id_user})

def user_edit_password(request, id_user):
    if not request.user.is_authenticated:
        return redirect('login')

    user_instance = get_object_or_404(User, id=id_user)
    form = forms.UserEdidPasswordForm()

    if request.method == 'POST':
        form = forms.UserEdidPasswordForm(request.POST)   
        if form.is_valid():
            new_password = form.cleaned_data['password']
            user_instance.password = make_password(new_password)
            user_instance.save()
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect('user_list')

    return render(request, 'users/user_edit_password.html', {'form': form, 'id_user': id_user})
 

def user_delete(request, id_user):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        user_instance = get_object_or_404(User, id=id_user)
        user_instance.delete()
        messages.success(request, 'Usuário excluido com sucesso!')
        return redirect('user_list')
    
    return render(request, 'users/user_delete.html', {'id_user': id_user})

    
    pass

