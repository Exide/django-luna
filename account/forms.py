from django.forms import ModelForm
from django.forms import PasswordInput
from django.contrib.auth.models import User
from models import Profile

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {'password': PasswordInput()}

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']