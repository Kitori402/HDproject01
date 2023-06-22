"""HEALTHproject02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from ONLINEdata import views
from ACCOUNTS import views
from django.urls import path ,re_path as url

urlpatterns = [
    path('',include('MEDICAL01.urls')),
    path('admin/', admin.site.urls),
    path('ONLINEdata/',include('ONLINEdata.urls')),
    path('pharmacy/',include('PHARMACY.urls')),
    path('accounts/',views.MuhimbiliSocialHomePage.as_view(),name='home'),
    path('accounts/',include('ACCOUNTS.urls' , namespace='accounts')),
    path('accounts/',include('django.contrib.auth.urls')),
    url('test/',views.TestPage.as_view(), name='test'),
    url('thanks/',views.ThanksPage.as_view(), name='thanks'),
    url('posts/',include('POSTS_SM.urls' , namespace='posts')),
    url('groups/',include('GROUPS_SM.urls' , namespace='groups')),
    path('management/',include('HOSPITAL_MANAGEMENT.urls')),



]
