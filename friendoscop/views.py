from django.shortcuts import render, redirect
from django.http import HttpRequest
from friendoscop.forms import LoginForm
from datetime import datetime

def home(request):
    return render(request, 'home.html', {"current_datetime": datetime.now})


def login(request: HttpRequest):
    if len(request.POST) > 0:
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('/home')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
