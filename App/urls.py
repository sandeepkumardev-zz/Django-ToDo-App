from django.urls import path
from App import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('add_item/', views.add_item, name="add_item"),
    path('delete/<int:todo_id>', views.delete, name="delete"),
]
