from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .models import Member
from django.contrib.auth.hashers import make_password

# Create your views here.
def index(request):
    # html = '<h2>Hello Django</h2>'
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
    # name = request.GET.get('username')  #讀不到 username 回傳 None
    # if name == None:
    #     name = 'Django'
    # html = f'<h2>Hello {name}</h2>'

    # response = HttpResponse(html)
    # response.status_code = 200
    # [{},{}]
    # response['Contwnt-Type'] = 'application/json'
    # response.encoding = 'utf-8'


    # return HttpResponse(html)
    # return render(request, 'member/index.html')

    # 資料庫的操作
    # 資料新增
    # Member.objects.create(
    #     member_name = "qweasd",
    #     member_password = "123456",
    #     member_birth = "2028-04-28",
    #     member_email = "qweasd@gmail.com"
    # )
    
    # 讀取所有會員資料
    # members = Member.objects.all()
    # print(members)

    # 讀取單筆會員資料
    # member = Member.objects.get(member_id=2)
    # print(member)

    # 修改資料
    # 1. 先找到要修改的資料
    # member = Member.objects.get(member_id=1)
    # 2.進行修改
    # member.member_name = "Jaymom"
    # member.member_birth = "1962-02-10"
    # member.save()
    # 3.將修改後結果更新於資料庫

    # 刪除資料
    # 1. 先找到要修改的資料
    # member = Member.objects.get(member_id=5)
    # 2.進行刪除
    # member.delete()
    # return HttpResponse("資料庫操作練習")

    #讀取會員所有資料
    members = Member.objects.all()
    return render(request, "member/index.html", {"members":members} )

def register(request):


    if request.method == 'POST':
        # 接收使用者上傳的資料
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        password = request.POST.get('userpassword')
        birth = request.POST.get('userbirth')


        # 接收上傳的檔案
        userphoto = request.FILES.get('userphoto')

        # # 檔案名稱
        file_name = userphoto.name
        # # 檔案大小
        # file_size = userphoto.size
        # # 檔案類型
        # file_type = userphoto.content_type

        # print(name)
        # print(email)
        # print(userphoto)
        # print(f'檔案名稱: {file_name}')
        # print(f'檔案大小: {file_size}')
        # print(f'檔案類型: {file_type}')

        # 將上傳檔案儲存到 uploads資料夾
        fs = FileSystemStorage()
        upload_file = fs.save(file_name, userphoto)
        # print(f'upload file: {upload_file}')


        # 將表單傳過來的資料寫進資料庫
        Member.objects.create(
            member_name = name,
            member_password = make_password(password),
            member_birth = birth,
            member_email = email,
            member_avatar = upload_file
        )
        return redirect('member:index')
        # return HttpResponseRedirect('/member/')
        


    return render(request, 'member/register.html')

# /edit/?id=2
def edit(request):
    if request.method == "POST":
        # 接收使用者上傳的資料
        id = request.POST.get("userid")
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        birth = request.POST.get('userbirth')
        # 接收上傳的檔案
        userphoto = request.FILES.get('userphoto')
        file_name = userphoto.name
        # 將上傳檔案儲存到 uploads資料夾
        fs = FileSystemStorage()
        upload_file = fs.save(file_name, userphoto)
        # 修改到資料庫
        member = Member.objects.get(member_id=id)
        member.member_name = name
        member.member_email = email
        member.member_birth = birth
        member.member_avatar = upload_file
        member.save()
        return redirect('member:index')


    id = request.GET.get("id", 1)
    member = Member.objects.get(member_id=id)
    return render(request, "member/edit.html", {"member":member})

# /delete/1
def delete(request, id):
    member = Member.objects.get(member_id=id)
    member.delete()
    return redirect('member:index')

def mobile(request):
    return HttpResponse('<h2>Mobile Page</h2>')

