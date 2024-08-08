"""
URL configuration for secondproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# from home import views
# from member import views as member_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', include('home.urls')),  #載入 home 下面的 urls.py
    #https://127.0.0.1:8000/member/
    path ('member/', include('member.urls')),  #載入 member 下面的 urls.py
    #https://127.0.0.1:8000/store/
    path ('store/', include('myapp.urls')),  #載入 myapp 下面的 urls.py
]
 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)