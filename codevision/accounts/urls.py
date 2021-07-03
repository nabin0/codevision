
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.loginHandle, name="register"),
    path('logout/', views.logoutHandle, name="register"),
]
