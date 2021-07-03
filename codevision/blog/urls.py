
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    # Api for comments
    path('postComments/', views.postComments, name="postComment"),


    path('', views.blogHome, name="blogHome"),
    path('<str:slug>', views.blogPost, name="blogPost"),
]
