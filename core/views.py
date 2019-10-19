from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import (authenticate, login, logout,)
from django.contrib.auth.decorators import login_required
import time
import csv


# #Controlador Login
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')

    print(request.user.is_authenticated)
    title = "Login"
    form = UserLoginForm(request.POST or None)
    localtime = time.asctime(time.localtime(time.time()))

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated)
        print(username)
        return redirect('/dashboard/')
    return render(request, 'core/login.html', {"form": form, "title": title, "localtime": localtime})


# #Controlador Logout
@login_required(login_url='logout')
def logout_view(request):
    logout(request)
    return redirect('/login/')


# # Controlador de Dashboard
@login_required(login_url='logout')
def dashboard(request):
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)
    current_user = request.user
    usuario = User.objects.get(id=current_user.id)
    last_login = usuario.last_login
    print(last_login)

    with open('btcusd.csv') as file:
        reader = csv.reader(file)
        count = 0
        data_list = []
        for row in reader:
            # usd_btc = [row[0], float(row[2]), float(row[3]), float(row[4]), float(row[5])]
            usd_btc = [row[0], row[2], row[3], row[4], row[5]]
            print(usd_btc)
            if count > 1772:
                break
            count += 1
            data_list.append(usd_btc)

        print('\n --- \n\n --- \n')
        data_chart = data_list[::-1]
        print(data_chart)

    context = {
        "localtime": localtime,
        "last_login": last_login,
        "data_chart": data_chart,
    }
    return render(request, 'core/dashboard.html', context)


# # Controlador de Cryptos
@login_required(login_url='logout')
def cryptos(request):
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)
    current_user = request.user
    usuario = User.objects.get(id=current_user.id)
    last_login = usuario.last_login
    print(last_login)

    context = {
        "localtime": localtime,
        "last_login": last_login,
        # "data_chart": data_chart,
    }
    return render(request, 'core/crypto.html', context)


# # Controlador de Trading Bot
@login_required(login_url='logout')
def bot(request):
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)
    current_user = request.user
    usuario = User.objects.get(id=current_user.id)
    last_login = usuario.last_login
    print(last_login)

    context = {
        "localtime": localtime,
        "last_login": last_login,
        # "data_chart": data_chart,
    }
    return render(request, 'core/bot.html', context)
