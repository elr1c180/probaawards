import random
from django.shortcuts import render, redirect
from .forms import LoginForm, RegForm, ResetForm, NewPassword, LoginFormMod
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail  

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        # Проверка валидности данных формы:
        if form.is_valid():
            email =  form.cleaned_data['email']
            password = form.cleaned_data['password']

            if User.objects.filter(email=email, password=password):
                username = User.objects.get(email = email).username
                user = authenticate(request, username = username, password = password)
                login(request, User.objects.get(email=email))
                return redirect('/')
            else:
                messages.error(request,'Неправильный Email или пароль')
    return render(request, 'login.html', {'form': LoginForm})

def reg(request):

    if request.method == 'POST':
        form = RegForm(request.POST)

        # Проверка валидности данных формы:
        if form.is_valid():
            name = form.cleaned_data['name']
            company = form.cleaned_data['company']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password =  form.cleaned_data['password']
            
            if Member.objects.filter(email=email):
                messages.error(request,'Пользователь с таким Email уже существует !')
            username = random.randint(1, 99999)
            user = User.objects.create(
                username = username,
                password = password,
                email = email
            )

            mem = Member.objects.create(
                user= user,
                name = name,
                company = company,
                email = email,
                phone = phone,
                password = password
            )
            
            us_auth = authenticate(username, password=password)
            login(request, user)
            
            return redirect('/')
    return render(request, 'reg.html', {'form': RegForm})

def main(request):
    if request.user.is_authenticated:
        user = Member.objects.get(user=request.user)
        return render(request, 'main.html', {'user':user})
    else:
        return redirect('login/')
    
def work(request):
    user = Member.objects.get(user=request.user)
    return render(request, 'work.html', {'user':user})

def logout_view(request):
    logout(request)
    messages.error(request,"Вы вышли из аккаунта")
    return redirect('/')

def reset(request):
    if request.method == 'POST':
        
        form = ResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                id_off = random.randint(1,99999)
                ResetPassword.objects.create(
                    user = User.objects.get(email=email),
                    id_off = id_off
                )
                send_mail('Сброс пароля', f'Ваша ссылка для восстановления пароля: dvahhsob.beget.tech/reset_pass/{id_off}', 'proba.awards@yandex.ru',[email])
                messages.error(request,'Письмо с ссылкой для сброса пароля отправлено вам на почту!')
            except Exception as e:
                print(e)
                messages.error(request,'Проверьте правильность почты!')

    return render(request, 'reset.html', {'form': ResetForm})

def reset_pass_check(request, id):
    id = id
    if ResetPassword.objects.filter(id_off=id):
        if request.method == 'POST':
            form = NewPassword(request.POST)
            if form.is_valid():
                password = form.cleaned_data['password']
                user = ResetPassword.objects.get(id_off=id).user
                mem = Member.objects.get(user=user)
                mem.password = password
                user.password = password
                user.save()
                mem.save()
                n = ResetPassword.objects.get(id_off=id).delete()
                
                messages.error(request, 'Ваш пароль успешно сброшен!')
                return redirect('/login/')
        return render(request, 'new_pass.html', {'form': NewPassword})
    else:
        return redirect('/')


def login_mod(request):
    if request.method == 'POST':
        form = LoginFormMod(request.POST)
        # Проверка валидности данных формы:
        if form.is_valid():
            username =  form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                if User.objects.filter(username=username) and len(Member.objects.filter(user=User.objects.get(username=username))) == 0:
                    login(request, User.objects.get(username=username))
                    return redirect('/mod/')
                else:
                    messages.error(request, 'Проверьте правильность введенных данных')
            except Exception as e:
                messages.error(request, 'Проверьте правильность введенных данных')
    return render(request, 'login_mod.html', {'form':LoginFormMod})


def mod(request):
    return render(request, 'main_mod.html')