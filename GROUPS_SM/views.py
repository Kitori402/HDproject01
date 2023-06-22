
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect

from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db import IntegrityError
from ACCOUNTS.models import User

from django.contrib.auth.models import User
 

from . import models
#importing the model enables the linking of the views to the model
from GROUPS_SM.models import Group, GroupMember


# Create your views here.
# CBV are also included
 

#the view below is connected to the Group.model thus when called enbles the user to make/edit the listed fields
class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields = ('name', 'description') 
    model = Group

#shows the details of the group like posts .... through the CBV fx
class SingleGroup(generic.DetailView):
    model = Group
    template_name = 'groups_sm/group_details.html'

class ListGroups(generic.ListView):
    model = Group

class JoinGroup(LoginRequiredMixin, generic.RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get("slug"))
        
        try:
          
            GroupMember.objects.create(user=self.request.user,group=group)

        except IntegrityError:
            messages.warning(self.request,("Warning, already a member of {}".format(group.name)))

        else:
            messages.success(self.request,"You are now a member of the {} group.".format(group.name))

           

        template_name = 'groups_sm/group_details.html'

        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, generic.RedirectView):
    
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})
    
    #to check if the user bellongs in the grp
    def get(self,request,*args,**kwargs):

        try:
            membership = models.GroupMember.objects.filter(
                user=self.request.user,
                group__slug=self.kqargs.get('slug')
            ).get()
        except models.GroupMember.DoesNotExist:
            messages.warning(self.request,'Sorry you are not in this group')
        else:
            membership.delete()
            messages.success(self.request,'you have left the group')
        return super().get(request,*args,**kwargs)


      
