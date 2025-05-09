from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to a dashboard or home page after login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'accounts/signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'accounts/signup.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'accounts/signup.html')
        
        # Create the user
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        # Log the user in and redirect
        login(request, user)
        messages.success(request, "Account created successfully!")
        return redirect('login')  # Redirect to login page after signup
    
    return render(request, 'accounts/signup.html')
