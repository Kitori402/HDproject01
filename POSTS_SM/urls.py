from django.urls import path ,re_path as url
from . import views
from django.conf import settings

#for template tagging
app_name = 'POSTS_SM'

urlpatterns =[
    url('posts/',views.PostList.as_view(), name='all'),
    url ('new/',views.CreatePost.as_view(), name='create'),
    url('by/(?P<username>[-\w]+)',views.UserPosts.as_view(), name='for_user'),
    url('by/(?P<username>[-\w]+)/(?P<pk>\d+)/',views.PostDetail.as_view(), name='single'),
    url('delete/(?P<pk>\d+)/', views.DeletePost.as_view(), name='delete')
] 
        