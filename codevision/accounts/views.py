from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from .models import UserDetail
from django.contrib import auth, messages

def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists() or username == "":
                messages.info(request, "Username cannot be Blank Or already taken")
                return redirect("/accounts/register/")
            else:
                if User.objects.filter(email=email).exists() or email == "":
                    messages.info(request, "Email already registered")
                    return redirect("/accounts/register/")
                else:
                    userDet = UserDetail(first_name=first_name,last_name=last_name,username=username,email=email,phone=phone,gender=gender, password=password, confirm_password=confirm_password)
                    userDet.save()
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                    user.save()
        else:
            messages.info(request, "Password Did not match")
            return redirect("/accounts/register/")
    return render(request, "accounts/register.html")

def loginHandle(request):
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Login credentials Wrong. Please try again with correct information.")
            return redirect("/accounts/loginHandle/")
    
    return render(request, "accounts/login.html")

def logoutHandle(request):
    auth.logout(request)
    return redirect("/")