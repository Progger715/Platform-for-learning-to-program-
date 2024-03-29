"""lms_programming URL Configuration

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
from django.urls import path

from handler_code import view_django
from users.views import api_view_login, api_view_registration
from handler_code.views import api_view_ariphmetic_task, api_view_condition_task, api_view_loop_tasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_django.rec),
    path('api/login', api_view_login.ApiViewLogin.as_view()),
    path('api/registration', api_view_registration.ApiViewRegistration.as_view()),
    path('api/aripmetic_task', api_view_ariphmetic_task.ApiViewAriphmeticTask.as_view()),
    path('api/condition_task', api_view_condition_task.ApiViewConditionTask.as_view()),
    path('api/loop_task', api_view_loop_tasks.ApiViewLoopTask.as_view()),
]
