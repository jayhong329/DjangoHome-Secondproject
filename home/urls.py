from django.urls import path
from home import views

app_name = 'home'
urlpatterns = [
    path ('', views.index, name = 'index'), # http://127.0.0.1:8000/
    path('home/',views.index),  #https://127.0.0.1:8000/home/
    path('countries/',views.countries),  #https://127.0.0.1:8000/countries/
    path('about/',views.about),  #https://127.0.0.1:8000/about/
    path('about/<int:year>',views.about),  #https://127.0.0.1:8000/about/2100
    path('categories/',views.categories),  #https://127.0.0.1:8000/categories/
    path('cities/',views.cities),  #https://127.0.0.1:8000/cities/

]