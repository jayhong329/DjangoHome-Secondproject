from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Category

# Create your views here.

def index(request):
    # return HttpResponse('<h2>我的APP 首頁</h2>')
    title= 'hello myapp'
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
    title = '資料庫的讀取'

    # 跟 Model 要資料
    categories = Category.all()
    categories_one = Category.single(1)
    # categories_insert = Category.create("Jeremy")
    # categories_update = Category.update(20, "ROSA")
    categories_delete = Category.delete(23)
    # print(categories)

    # 打資料傳給 templates ，透過 render() 第三個參數，傳入一個{}結構的資料
    # return render(request, 'myapp/show.html', {'title': title, 'categories': categories})
    return render(request, 'myapp/show.html', locals())


def abc(request):
    user = {'name':'Jack','age':40}
    users = [{'name':'Jack','email':'Jack@gmail.com','age':32},
             {'name':'Mary','email':'Mary@gmail.com','age':26},
             {'name':'Tom','email':'Tom@gmail.com','age':41},
             {'name':'Fion','email':'Fion@gmail.com','age':29}]
    title = 'Template 練習'
    return render(request, 'myapp/abc.html', locals())
    # return render(request, 'myapp/abc.html', {'user': user,'users': users,'title': title})
