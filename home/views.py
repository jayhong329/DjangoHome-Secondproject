from django.shortcuts import render
from .models import Sakila   #.models 就是同一路徑 底下的models
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    # 讀取透過 GET 傳過來的 ?id= 10 的資料
    id = request.GET.get('id')
    country = ''

    if request.method == 'POST':
        # 讀取透過 POST 傳過來的表單資料
        country = request.POST.get('country')

    return render(request, 'home/index.html', {'id':id, 'country': country})

def about (request, year = None):
    if year == None :
        html = '<h2> 關於 {} 年的我們 </h2>'.format(datetime.now().year)
    else :
        html = '<h2> 關於 {} 年的我們 </h2>'.format(year)
    print(html)

    return render(request, 'home/about.html')

def categories(request):
    # 跟Model要資料
    categories = Sakila.categories()
    # render()第三個參數，把資料傳給 Template
    return render(request, 'home/categories.html', {'categories':categories})

def countries(request):
    # 跟Model要資料
    countries = Sakila.countries()
    print(countries)
    # render()第三個參數，把資料傳給 Template
    return render(request, 'home/countries.html', {'countries':countries})

def cities(request):
    # print(request.GET)  #key=value&key=value => {'key':['value']}
    # print(request.GET['id'])
    id = request.GET.get('id', 1)
    country = request.GET.get('country', '')
    # print(id)
    # print(country)

    # 跟Model要資料
    cities = Sakila.cities(id)
    # render()第三個參數，把資料傳給 Template
    return render(request, 'home/cities.html', {'cities':cities, 'country':country})



# def cities(request):
#     # print(request.GET)  #key=value&key=value => {'key':['value']}
#     # print(request.GET['id'])
#     id = request.GET.get("id",1)
#     country = request.GET.get("country", "")

#     # 跟Model要資料
#     cities = Sakila.cities(id)
#     print(cities)
#     # render()第三個參數，把資料傳給 Template
#     return render(request, 'cities.html', {'cities':cities, 'country':country})




def register(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        print(name)
        print(email)

    return render(request, 'member/register.html')
def mobile(request):
    return HttpResponse('<h2>Mobile 專屬</h2>')


