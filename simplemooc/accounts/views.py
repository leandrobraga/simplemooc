from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm
from .forms import EditAccountForm
from .forms import PasswordResetForm
from .models import PasswordReset
from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from simplemooc.courses.models import Enrollment


User = get_user_model()


@login_required
def dashboard(request):

    template_name = "accounts/dashboard.html"
    context = {}

    return render(request, template_name, context)


def register(request):

    template_name = "accounts/register.html"

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = RegisterForm()

    context = {'form': form}

    return render(request, template_name, context)


def password_reset(request):
    template_name = "accounts/reset_password.html"
    context = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form

    return render(request, template_name, context)


def password_reset_confirm(request, key):

    template_name = "accounts/reset_password_confirm.html"
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)


@login_required
def edit(request):
    template_name = "accounts/edit.html"
    context = {}
    if request.method == "POST":
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            #form = EditAccountForm(instance=request.user)
            #context['success'] = True
            messages.success(request, "Os dados da conta foram alterados com sucesso")
            return redirect("accounts:dashboard")
    else:
        form = EditAccountForm(instance=request.user)

    context['form'] = form
    return render(request, template_name, context)


@login_required
def edit_password(request):
    template_name = "accounts/edit_password.html"
    context = {}
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form

    return render(request, template_name, context)
