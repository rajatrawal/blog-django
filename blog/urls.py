from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogPost/<int:id>/', views.blogPost, name='blogPost'),
    path("postComment",views.postComment,name="postComment")
]
