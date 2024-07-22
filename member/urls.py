from django.urls import path
from member import views

urlpatterns = [
    path('', views.index ),   # http://127.0.0.1:8000/member/
    path('register/', views.register ),   # http://127.0.0.1:8000/member/register
    path('mobile/', views.mobile ),   # http://127.0.0.1:8000/member/mobile

]