from django.urls import path
from myapp import views

urlpatterns = [
    # path('比對的路徑', '要執行的function')
    #https://127.0.0.1:8000/store/
    path('', views.index),

    #https://127.0.0.1:8000/store/detail/uuid
    path('details/<uuid:product_id>', views.details),
    
    #https://127.0.0.1:8000/store/about/
    path('about/', views.about),
    
    #https://127.0.0.1:8000/store/about/2000
    path('about/<int:year>', views.about),
    
    #https://127.0.0.1:8000/store/blog/2024/7/1
    path('blog/<path:publish>', views.blog),

    #https://127.0.0.1:8000/store/course/
    path('course/<slug:course_name>', views.course),
]