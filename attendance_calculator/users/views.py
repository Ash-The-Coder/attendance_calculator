from django.shortcuts import render

# Create your views here.

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

@login_required
def welcome(request):
    username = request.user.username
    return render(request, 'welcome.html', {'username': username})

def custom_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration.html', {'form': form})

@login_required
def profile(request):
    # Your logic to retrieve and display the user's profile information
    return render(request, 'profile.html')