from django.shortcuts import render, redirect   
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.

def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account created for {username}!")
            return redirect('profile')
    else:
        form = UserRegisterForm()

    return render(request, 'user_authentication/register.html', {'form':form})

@login_required
def profile(request):
    return render(request,'user_authentication/profile.html')

@login_required
def logout_view(request):
    return render(logout(request),'user_authentication/logout.html')