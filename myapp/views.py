from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
    # return HttpResponse('<h2>我的APP 首頁</h2>')
    title= 'hello django'
    text = "a description, either true or imagined, of a connected series of events a description, either true or imagined, of a connected series of events a description, either true or imagined, of a connected series of events"
    now = datetime.now()
    id = '123e4567-e89b-12d3-a456-426655440000'
    # return render(request, 'myapp/index.html', {'title': title, 'now':now} )
    return render(request, 'myapp/index.html', locals() )


# 2000 會傳給 year 這個參數
def about(request, year=datetime.now().year):
    # return HttpResponse(f'<h2>ABOUT {year}</h2>')
    return render(request, 'myapp/about.html', {'year': year} )

# uuid 是唯一辨識碼
def details(request, product_id=''):
    return HttpResponse(f'<h2>讀出商品編號{product_id}的商品</h2>')

# publish => 2024/7/1
def blog(request, publish= None):
    return HttpResponse(f'<h2>讀取 {publish} 的文章</h2>')

# course_name => python-web-framework
def course(request, course_name= None):
    return HttpResponse(f'<h2>課程名稱: {course_name}</h2>')

def member_info(request, course_name= None):
    return render(request, 'myapp/member_info.html')

def show(request):
    title = 'store show'
    return render(request, 'myapp/show.html', {'title': title})