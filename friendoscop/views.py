from django.shortcuts import render
# from django.http import HttpResponse
from datetime import datetime

def welcome(request):
    return render(request, 'welcome.html', {"current_datetime": datetime.now})
