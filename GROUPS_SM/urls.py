from django.urls import path ,re_path as url
from . import views
from django.conf import settings



#template Tagging
app_name = 'GROUPS_SM'

urlpatterns =[
    url('groups/',views.ListGroups.as_view(), name='all'),
    url ('new/',views.CreateGroup.as_view(), name='create'),
    url('posts/in/(?P<slug>[-\w]+)/',views.SingleGroup.as_view(), name='single'),
    url(r"join/(?P<slug>[-\w]+)/$",views.JoinGroup.as_view(),name="join"),
    url('leave/(?P<slug>[-\w]+)/',views.LeaveGroup.as_view(),name='leave'), 
] 
        