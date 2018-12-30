from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('add/', views.addNewTodo, name = 'add'),
    path('Complete/<todo_id>/', views.CompleteTodo, name = 'complete'),
    path('delete/', views.DeleteTodo, name = 'delete'),
]
