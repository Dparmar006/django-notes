from django.urls import path

# views
from .views import RegisterUser, test

urlpatterns = [
    path('',RegisterUser.as_view(), name='My notes application'),
    path('test/',test, name='successful'),
    
]
