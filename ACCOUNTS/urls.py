from django.urls import path ,re_path as url
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views


#template Tagging
app_name = 'ACCOUNTS'

urlpatterns =[
    url('login/',auth_views.LoginView.as_view(template_name='social_media/login.html'), name='login'),
    url ('logout/',auth_views.LogoutView.as_view(), name='logout'),
    url('signup/',views.SignUp.as_view(), name='signup'), 
] 
        