from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from . import forms
from django.urls import reverse_lazy 
#reverse_lazy is a model used during logins and log outs for directions

# Create your views here. 
#we are also going to use (class based views)

#it displays the home social pages in CBV
class MuhimbiliSocialHomePage(TemplateView):
    template_name='social_media/social.html'

# to creates new user
class SignUp(CreateView): 
    form_class= forms.UserCreateForm
    success_url = reverse_lazy('login') #that means that once the user has sucessfully signUp he or she is directed back to the LOGIN page
    template_name = 'social_media/sign_up.html'


class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'   