from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpRequest
from django.contrib import auth

from .forms import LoginForm


def login(request: HttpRequest):
    title = 'Вход на сайт'

    login_form = LoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')

    content = {
        'title': title,
        'login_form': login_form
    }
    return render(request, 'authapp/login.html', content)


def logout(request: HttpRequest):
    auth.logout(request)
    return HttpResponseRedirect('/')


def redirect_to_login(request: HttpRequest):
    return HttpResponseRedirect('/auth/login')


def register(request: HttpRequest):
    return HttpResponseRedirect('/')


def edit(request: HttpRequest):
    return HttpResponseRedirect('/')
