from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .forms import RegisterForm, LoginForm, ProfileForm


def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to='app_quotes:quotes')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='app_quotes:quotes')
        else:
            return render(request, 'app_users/login.html', context={"form": form})

    return render(request, 'app_users/register.html', context={"form": RegisterForm()})

def loginuser(request):
    if request.user.is_authenticated:
       return redirect(to='app_quotes:quotes')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='app_users:login')

        login(request, user)
        return redirect(to='app_quotes:quotes')

    return render(request, 'app_users/login.html', context={"form": LoginForm()})

@login_required
def logoutuser(request):
    logout(request)
    return render(request, 'app_users/logout.html', context={})

@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='app_users:profile')

    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'app_users/profile.html', {'profile_form': profile_form})


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'app_users/password_reset.html'
    email_template_name = 'app_users/password_reset_email.html'
    html_email_template_name = 'app_users/password_reset_email.html'
    success_url = reverse_lazy('app_users:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'app_users/password_reset_subject.txt'
    