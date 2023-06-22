from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from braces.views import SelectRelatedMixin
from django.http import Http404

from . import models
from . import forms

from django.contrib import messages


from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

#list of posts in a group
class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ('user','group')

#the list of posts of the user
class UserPosts(generic.ListView):
    model = models.Post
    template_name = 'posts_sm/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related("posts").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
          raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['post_user'] = self.post_user
       return context
    


class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ('user', 'group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__name__iexact=self.kwargs.get('username'))


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('message', 'group')
    model = models.Post

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
    

class DeletePost(LoginRequiredMixin, SelectRelatedMixin,generic.DeleteView):
    model = models.Post
    select_related = ('user', 'group')
    success_url = reverse_lazy('posts:all')  #uses template tagging

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)
    
    def delete(self,*args,**kwargs):
        messages.success(self.request,'post Deleted')
        return super().delete(*args,**kwargs)


