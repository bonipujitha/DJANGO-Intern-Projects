"""GVPCPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('facultylogin/', views.facultylogindef, name='faclogin'),
    path('floginaction/', views.floginaction, name='floginaction'),
    path('fsignupaction/', views.fsignupaction, name='fsignupaction'),
    path('fviewprofile/', views.fviewprofile, name='fviewprofile'),
    path('fupdateprofile/', views.fupdateprofile, name='fupdateprofile'),
    path('fupdateaction/', views.fupdateaction, name='fupdateaction'),
    path('fachome/', views.fachome, name='fachome'),
    path('faclogout/', views.faclogout, name='faclogout'),
    
    
    
    
    
]
