"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('home.urls')),
    path('', views.login_view, name='login_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('addlist/', views.addlist, name='addlist'),
    path('additem/', views.additem, name='additem'),
    path('list/<int:id>/<slug:slug>/', views.list_detail, name='list_detail'),
    path('list_detail/',views.list_detail, name = 'list_detail')
]
