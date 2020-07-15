from django.urls import path

# views
from . import views

urlpatterns = [
    path('register/', views.RegisterUser, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('',views.home, name='HomePage'),
    
    path('delete/<int:pk>/',views.delete_note, name='DeleteNote'),
    path('edit/<int:pk>/',views.edit_note, name='EditNote'),
    
]
