# dashboard/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def user_home(request):
    return render(request, 'dashboard/dashboard.html')
