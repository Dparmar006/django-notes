from django.shortcuts import render, HttpResponse
# models
from django.contrib.auth.models import User
# form
from .forms import NoteUserCreationForm
# generic views

from django.views.generic import CreateView, FormView

# Create your views here.

class RegisterUser(FormView):
  template_name = 'notes/RegisterUser.html'
  form_class = NoteUserCreationForm
  success_url = 'test'

def test(request):
  return HttpResponse('Done !')

