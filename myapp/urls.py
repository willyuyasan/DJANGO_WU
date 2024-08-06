"""
URL configuration for myapp project.

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
from django.urls import path, include #json views
from taskwu.views import greeting, signup, home, tasks, close_session, signin, create_task, task_details #Http views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('taskwu.urls')),

    path('',home, name='home'),
    path('signup/',signup, name='signup'),
    path('tasks/',tasks, name='tasks'),
    path('task/create/',create_task, name='create_task'),
    path('task/<int:task_id>/',task_details, name='task_details'),
    path('close_session/',close_session, name='close_session'),
    path('signin/',signin, name='signin'),
    
]
