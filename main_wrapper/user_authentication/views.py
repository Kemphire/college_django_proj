from django.shortcuts import render, redirect   
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.

def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account created for {username}!")
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'user_authentication/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save() 
            p_form.save()
            messages.success(request, f"You account has been updated successfully!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'user_authentication/profile.html',context)

@login_required
def logout_view(request):
    return render(logout(request),'user_authentication/logout.html')

class ResetPasswordView(PasswordResetView,SuccessMessageMixin):
    template_name = "user_authentication/passwd_reset.html"
    email_template_name = "user_authentication/passwd_reset_email.html"
    subject_template_name = "user_authentication/passwd_reset_subject.html"
    success_message = "An email send to you with the detailed instruction, with a link to reset your password\nFeel free to contact with us if you feel that you are not able to change it"
    success_url = reverse_lazy('blog-home')