from django.urls import path
from . import views
from django.conf import settings

#TEMPLATE TAGGING IS BELLOW
app_name = 'PHARMACY'

urlpatterns =[
    path('', views.pharmacy , name='pharmacy')
]