from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
        path('todoapp/modify/<str:pk>',views.modifyTask, name='modify-task'),
]