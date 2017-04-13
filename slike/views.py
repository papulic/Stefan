# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Slike
from .forms import UserForm
from django.http import HttpResponseRedirect

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'slike/login.html')
    else:
        slike = Slike.objects.all()

        return render(request, 'slike/index.html', {
            'slike': slike,
        })

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/slike')
            else:
                return render(request, 'slike/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'slike/login.html', {'error_message': 'Invalid login'})
    return render(request, 'slike/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {"form": form}
    return render(request, 'slike/login.html', context)
