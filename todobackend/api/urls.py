from django.urls import path
from . import views


urlpatterns = [
     path('todo/' , views.TodoListCreate.as_view()),
     path("todo/<int:pk>" , views.TodoRetrieveUpdateDestroy.as_view()),
     path("todo/<int:pk>/complete" , views.TodoToggleComplete.as_view()),
     path("signup/" , views.signup),
     path('login/' , views.login),
]
