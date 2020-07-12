from django.shortcuts import render, HttpResponse, redirect
# models
from django.contrib.auth.models import User
from .models import Notes
# form
from .forms import AddNotesForm, NoteUserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# messages
from django.contrib import messages

# authentication
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

def RegisterUser(request):
  if request.method == 'POST':
    form = NoteUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      user_name = form.cleaned_data.get('username')
      messages.success(request, f'{user_name} has been registered ! ' )
      redirect('HomePage')
  else:
    form = NoteUserCreationForm()
  return render(request, 'notes/RegisterUser.html', {'form' : form})

def login_request(request):
  if request.method == 'POST':
    
    form = AuthenticationForm(request=request,data= request.POST)
    if form.is_valid():
      form_username = form.cleaned_data.get('username')
      form_password = form.cleaned_data.get('password')
      userLoginObject = authenticate(username=form_username, password = form_password)
      if userLoginObject is not None :
        login(request, userLoginObject)
        print('check')
        return redirect('HomePage')
      else:
        return redirect('login')
  else:
    form = AuthenticationForm()
  return render(request, 'notes/login.html', {'form' : form})

def logout_view(request):
  logout(request)
  return redirect('login')
  

def test(request):
  return HttpResponse('Done !')

@login_required
def home(request):
  if request.method == 'POST':
    form = AddNotesForm(request.POST)
    if form.is_valid():
      form_title = form.cleaned_data.get('title')  
      form_content = form.cleaned_data.get('content')  
      form_created_at = form.cleaned_data.get('created_at')  
      form_updated_at = form.cleaned_data.get('updated_at')  
      form_user = request.user

      qry = Notes.objects.create(title = form_title, content = form_content, created_at = form_created_at, updated_at = form_updated_at, created_by_id = form_user.id )
      qry.save()
      return redirect('HomePage')
  else:
    form = AddNotesForm()

  form_user = request.user
  notes = Notes.objects.filter(created_by_id = form_user).order_by('-pk')
  return render(request, 'notes/home.html', {'form' : form, 'notes' : notes})

@login_required
def delete_note(request,pk):
  note_id = pk
  messages.error(request, f'Note deleted !')
  Notes.objects.filter(pk=note_id).delete()

  return redirect('HomePage')

@login_required
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
      form_title = form.cleaned_data.get('title')  
      form_content = form.cleaned_data.get('content')  
      form_created_at = form.cleaned_data.get('created_at')  
      form_updated_at = form.cleaned_data.get('updated_at')  
      form_user = request.user

      qry = Notes.objects.create(title = form_title, content = form_content, created_at = form_created_at, updated_at = form_updated_at, created_by_id = form_user.id )
      qry.save()

      Notes.objects.filter(pk=note_id).delete()
      messages.success(request, f'Note updated !')
      return redirect('HomePage')
  else:
     form = AddNotesForm({
    'title' : title,
    'content' : content
  })

  return render(request, 'notes/home.html',{'notes' : notes, 'form' : form})
