from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
    return HttpResponse('<h2>我的APP 首頁</h2>')
    #return render(request, )

def about(request, year=datetime.now().year):
    return HttpResponse(f'<h2>ABOUT {year}</h2>')
