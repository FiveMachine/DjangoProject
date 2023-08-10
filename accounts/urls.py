from django.urls import path, include
from . import views

urlpatterns = [
    path("signupaccount/", views.signupaccount, name="signupaccount"),
    path("logout/" , views.logoutaccount , name="logoutaccount"),
    path("login/" , views.loginaccount , name="loginaccount"),
]
