from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from .utils import send_notification_email
import uuid
from django.shortcuts import render
#from .models import app_collection

# Create your views here.

def home(request):
    return render(request, "app/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists! Please try a different username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('home')
        
        if len(username) > 10:
            messages.error(request, "Username must be at most 10 characters.")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords did not match!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric.")
            return redirect('home')
        
        try:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            
            messages.success(request, "Your account has been successfully created.")
            
            # Welcome email
            # Email details for the new user
            user_subject = "Welcome to Our Page"
            user_message = f"Dear {fname+lname},\n\nThank you for registering your account . Here are your details:\nUsername: {username}\nEmail: {email}"
            user_recipient_list=[email]
            
            send_notification_email(user_subject, user_message, user_recipient_list)
            
            # subject = "Welcome to the app"
            # message = f"Hello {myuser.first_name}!!\n\nWelcome to the app!!\nThank you for visiting our website.\nWe have also sent you a confirmation email. Please confirm your email address to activate your account.\n\nThank you,\nThe App Team"
            
            # from_email = settings.EMAIL_HOST_USER
            # to_list = [myuser.email]
            # send_mail(subject, message, from_email, to_list, fail_silently=True)
            
            return redirect('signin')
        
        except IntegrityError:
            messages.error(request, "An error occurred during registration. Please try again.")
            return redirect('home')
    
    return render(request, "app/signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "app/index.html", {'fname': fname})
        
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('home')
    
    return render(request, "app/signin.html")

def signout(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('home')
