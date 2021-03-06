"""join_backend_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from joinboard.views import index, allTask, singlejson, logout_view, login_view, register_view, back_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('tasks/', allTask),
    path('tasks/<int:id>', singlejson),
    path('logout/', logout_view),
    path('login/', login_view),
    path('register/', register_view),
    path('back/', back_view)
]
