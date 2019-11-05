from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import (authenticate, login, logout,)
from django.contrib.auth.decorators import login_required
import time
import csv
import requests
import datetime


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

    fee_trx = 0.014
    fee = '1.4%'

    form = AssetTransacction(request.POST or None)
    if form.is_valid():
        trx = form.cleaned_data.get("trx")
        asst = float(form.cleaned_data.get("asst"))
        qty = float(form.cleaned_data.get("qty"))
        fee_trx = 0.014
        fee = '1.4%'
        asst_choiced = 2
        subtotal = qty*asst
        total = subtotal*1.014
        print(trx, asst, qty)
        print(total)

        Log.objects.create(date_time=localtime, user=current_user, transacction=trx, asset=asst, amount=total)
        context = {
            "trx": trx,
            "asst": asst,
            "qty": qty,
            "total": total,
        }

    context = {
        "form": form,
        "localtime": localtime,
        "last_login": last_login,
        "fee": fee,
    }

    form = AssetTransacction()

    return render(request, 'core/dashboard.html', context, {
        "form": form,
        "localtime": localtime,
        "last_login": last_login,
        "fee": fee,
    })


# # Controlador de Cryptos
@login_required(login_url='logout')
def cryptos(request):
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)
    current_user = request.user
    usuario = User.objects.get(id=current_user.id)
    last_login = usuario.last_login
    print(last_login)
    date_time = datetime.date.today
    print(date_time)

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
    date_time = datetime.date.today
    print(date_time)

    context = {
        "localtime": localtime,
        "last_login": last_login,
        # "data_chart": data_chart,
    }
    return render(request, 'core/bot.html', context)


# # Controlador de Trading Bot
@login_required(login_url='logout')
def logs(request):
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)
    current_user = request.user
    usuario = User.objects.get(id=current_user.id)
    last_login = usuario.last_login
    print(last_login)

    log_in = Log.objects.filter(transacction='Buy')
    print(log_in)

    log_out = Log.objects.filter(transacction='Sell')
    print(log_out)
    date_time = datetime.date.today
    print(date_time)

    ast = Asset.objects.filter()
    context = {
        "localtime": localtime,
        "last_login": last_login,
        "log_in": log_in,
        "log_out": log_out,
    }
    return render(request, 'core/logs.html', context)


@login_required(login_url='logout')
def register_data(request):
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)
    current_user = request.user
    usuario = User.objects.get(id=current_user.id)
    last_login = usuario.last_login
    print(last_login)

    log_in = Log.objects.filter(transacction='In')
    print(log_in)

    log_out = Log.objects.filter(transacction='Out')
    print(log_out)

    date_time = datetime.date.today
    print(date_time)

    context = {
        "localtime": localtime,
        "last_login": last_login,
        "log_in": log_in,
        "log_out": log_out,
    }
    return render(request, 'core/logs.html', context)



# f7f6fd1e-07d1-4a4e-875e-8d9d41936291