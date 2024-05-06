
from django.urls import path

from . import views

app_name = "app_users"

urlpatterns = [
    path('signup', views.signupuser, name='signup'),
    path('/login', views.loginuser, name='login'),
    path('/userlogout', views.logoutuser, name='userlogout')
]