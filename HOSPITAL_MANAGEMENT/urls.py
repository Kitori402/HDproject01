from django.urls import path
from . import views
from django.conf import settings

#TEMPLATE TAGGING IS BELLOW
app_name = 'HOSPITAL_MANAGEMENT'

urlpatterns =[
    path('', views.manage , name='manage'),
    path('abouts/', views.abouts , name='abouts'),
    path('contacts/', views.contacts , name='contacts'),
]