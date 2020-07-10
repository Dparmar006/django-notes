from django.urls import path

# views
from . import views

urlpatterns = [
    path('something',views.RegisterUser, name='My notes application'),
    path('test/',views.test, name='successful'),
    path('',views.home, name='HomePage'),
    
    path('delete/<int:pk>/',views.delete_note, name='DeleteNote'),
    path('edit/<int:pk>/',views.edit_note, name='EditNote'),
    
]
