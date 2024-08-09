from django.urls import path
from member import views

app_name = "member"
urlpatterns = [
    path('', views.index, name="index" ),   # http://127.0.0.1:8000/member/
    path('register/', views.register, name="create" ),   # http://127.0.0.1:8000/member/register
    path('edit/', views.edit, name="edit" ),   # http://127.0.0.1:8000/member/edit
    path('delete/<int:id>', views.delete, name="delete" ),   # http://127.0.0.1:8000/member/delete/
    path('mobile/', views.mobile, name="mobile" ),   # http://127.0.0.1:8000/member/mobile

]