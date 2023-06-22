from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm 
from ACCOUNTS.models import User
from django.urls import reverse_lazy
from django.urls import reverse


#the bellow imported model makes the  url to be more compatible to the browsers by removng spaces and other unwanted features in the string of url 
from django.utils.text import slugify

#returns the current user mode active ,enable to call things outside the user
from django.contrib.auth import get_user_model
user = get_user_model()

#allows the use of custom template .... thus allows to use the RELATED NAMES assigned to a class to call the class in template syntax and tagging
from django import template
register = template.Library()



# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(blank=True,default='')
    members = models.ManyToManyField(User,through='GroupMember')


    def __str__(self):
        return self.name
    
    #the super() saves all data in the class
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)
    

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name'] 
    

class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='memberships', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,related_name='user_groups', on_delete=models.DO_NOTHING)

    #for the string representation of the user shhown in the data base
    def __str__(self):
        return self.user.username
    
    class Meta:
        unique_together = ('group','user')
