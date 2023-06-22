#forms.py connect the forms for signing up or loggins to the views
# bellow are the forms like signings

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm #is like a signing model

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'USERNAME of CHOICE' #used to label the forms displayed to the user
        self.fields['email'].label = "Email Address"