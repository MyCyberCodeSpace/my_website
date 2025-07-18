"""
URL configuration for website project.

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
from django.urls import path
from mysiteapp.views import *

urlpatterns = [
    path('ascsda/sadasac/56sdas/sadsaygdue/sadas5645/', admin.site.urls),
    
    path('', homepage, name='home'),    
    path('about/', about, name='about'),
    
    path('portfolio/', portfolio, name='portfolio'),
    path('portfolio/<slug:slug>/', details_portfolio, name='details_portfolio'),
    
    path('documentation/', documentation, name='documentation'),
    path('documentation/<slug:slug>/', details_documentation, name='details_documentation'),
    
    path('support/', support, name='support'),

    path('privacy/', privacy, name='privacy'),
    path('terms/', terms, name='terms'),
]

handler404 = 'mysiteapp.views.handling404'