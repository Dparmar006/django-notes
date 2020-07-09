from django import forms
from .models import Notes
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NoteUserCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('first_name', 'username','password1', 'password2','email')

class AddNotesForm(forms.ModelForm):
  class Meta:
    model = Notes 
    fields = ('title','content')
    