from django.urls import path
from .import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('marked_as_done/<int:pk>/', views.marked_as_done , name='marked_as_done'),
    path('marked_as_undone/<int:pk>/', views.marked_as_undone , name='marked_as_undone'),
    path('edit_task/<int:pk>/', views.edit_task , name='edit_task'),
    path('delete_task/<int:pk>/', views.delete_task , name='delete_task'),
]