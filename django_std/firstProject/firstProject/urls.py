"""firstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from firstApp import views
from greetingapp import views as v1
from timeapp import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('hello/', views.display),
    path('mo/', views.good_M),
    path('eve/', views.good_E),
    path("go/", views.good_E),   #### 2nd url for good_E


    path('frnd/', v1.greetings_view),  ### multi app
    path('time/', v2.time_view),

]
