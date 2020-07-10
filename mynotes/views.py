from django.shortcuts import render, HttpResponse, redirect
# models
from django.contrib.auth.models import User
from .models import Notes
# form
from .forms import AddNotesForm
from .forms import NoteUserCreationForm

# messages
from django.contrib import messages
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
  messages.error(request, f'Note deleted !')
  Notes.objects.filter(pk=note_id).delete()

  return redirect('HomePage')

def edit_note(request,pk):
  note_id = pk
  notes_edit = Notes.objects.filter(pk=note_id)
  for c in notes_edit :
    title = c.title
    content = c.content

  notes = Notes.objects.all().order_by('-pk')
 
  if request.method == 'POST':
    form = AddNotesForm(request.POST)
    if form.is_valid():
      form.save()
      Notes.objects.filter(pk=note_id).delete()
      return redirect('HomePage')
  else:
     form = AddNotesForm({
    'title' : title,
    'content' : content
  })

  return render(request, 'notes/home.html',{'notes' : notes, 'form' : form})
