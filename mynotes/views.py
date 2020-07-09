from django.shortcuts import render, HttpResponse, redirect
# models
from django.contrib.auth.models import User
from .models import Notes
# form
from .forms import AddNotesForm
from .forms import NoteUserCreationForm
# generic views

from django.views.generic import CreateView, FormView, ListView

# Create your views here.

def RegisterUser(request):
  if request.method == 'POST':
    form = NoteUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
  else:
    form = NoteUserCreationForm()
  return render(request, 'notes/RegisterUser.html', {'form' : form})

def test(request):
  return HttpResponse('Done !')

def home(request):
  if request.method == 'POST':
    form = AddNotesForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('HomePage')
  else:
    form = AddNotesForm()

  
  notes = Notes.objects.all().order_by('-pk')
  return render(request, 'notes/home.html', {'form' : form, 'notes' : notes})


def delete_note(request,pk):
  note_id = pk
  Notes.objects.filter(pk=note_id).delete()
  return redirect('HomePage')

def edit_note(request,pk):
  note_id = pk
  id = Notes.objects.filter(pk=note_id).values_list('pk')
  title = Notes.objects.filter(pk=note_id).values_list('title')
  content = Notes.objects.filter(pk=note_id).values_list('content')
  print(id, title, content)
  notes = Notes.objects.all()
  form = AddNotesForm({'pk' : id, 'title' : title, 'content' : content})
  return render(request, 'notes/home.html',{'notes' : notes, 'form' : form})
