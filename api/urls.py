from django.urls import path
from .views import TodoCompletedList, TodoCreateList, TodoUpdateDestroyRetrieve, TodoComplete
from .views import signup, getTheToken,login

urlpatterns = [
    path('todos', TodoCreateList.as_view()),
    path('todos/<int:pk>', TodoUpdateDestroyRetrieve.as_view()),
    path('todos/<int:pk>/complete', TodoComplete.as_view()),
    path('todos/completed', TodoCompletedList.as_view()),

    path('sign-up', signup),
    path('test', getTheToken.as_view()),
    path('login',login)
]
