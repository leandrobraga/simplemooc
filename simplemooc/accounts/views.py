from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):

    template_name = "accounts/dashboard.html"

    return render(request, template_name)


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
