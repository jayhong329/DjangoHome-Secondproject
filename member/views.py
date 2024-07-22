from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    html = '<h2>Hello Django</h2>'
    # print(request.headers)  #用終端機 讀出所有 headers內含有的資料

    # 讀出 headers 裡面某類型的資料
    # print(request.headers.get('Content-Type'))
    # print(request.headers.get('User-Agent'))

    # 用網頁 讀出 headers 中所有的資料
    # html += '<ul>'
    # for key, value in request.headers.items():
    #     html += f'<li>{key}:{value}</li>'
    # html += '</ul>'

    # user_agent= request.headers.get('User-Agent')
    # print('Mobile' in user_agent)
    # if 'Mobile' in user_agent:
    #     return HttpResponseRedirect('/member/mobile/')
    

    # http method :  GET. POST. PUT. DELETE...
    # print(request.method)  # GET

    # 讀取透過GET 傳過來的資料 ?key=value
    name = request.GET.get('username')  #讀不到 username 回傳 None
    if name == None:
        name = 'Django'
    html = f'<h2>Hello {name}</h2>'

    return HttpResponse(html)
    # return render(request, 'member/index.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        # 接收上傳的檔案
        userphoto = request.FILES.get('userphoto')
        print(name)
        print(email)
        print(userphoto)

    return render(request, 'member/register.html')

def mobile(request):
    return HttpResponse('<h2>Mobile Page</h2>')