from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h2>我的APP 首頁</h2>')
    return render(request, )#