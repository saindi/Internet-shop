from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from user.forms import SignUpForm, SignInForm, EditUserDataForm, EditUserPasswordForm
from user.models import UserModel


@login_required()
def user_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'user/user.html')


def signin_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('user:profile_url'))

    if request.method == "POST":
        form = SignInForm(request.POST)

        if form.is_valid():
            login(request, form.user)
            if 'next' in request.GET:
                return HttpResponseRedirect(request.GET['next'])
            else:
                return HttpResponseRedirect(reverse_lazy('catalog:home_url'))
    else:
        form = SignInForm()

    return render(request, 'user/signin.html', {"form": form})


def signup_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('user:profile_url'))

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.create_user()
            return HttpResponseRedirect(reverse_lazy('user:signin_url'))
    else:
        form = SignUpForm()

    return render(request, 'user/signup.html', {"form": form})


@login_required()
def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)

    return HttpResponseRedirect(reverse_lazy('catalog:home_url'))


@login_required()
def deactivation_user_view(request: HttpRequest) -> HttpResponse:
    user = UserModel.objects.get(username=request.user.username)

    user.is_active = False
    user.save()

    logout(request)

    return HttpResponseRedirect(reverse_lazy('catalog:home_url'))


@login_required()
def edit_user_data_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = EditUserDataForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('user:profile_url'))
    else:
        form = EditUserDataForm(instance=request.user)

    return render(request, 'user/edit_user_data.html', {"form": form})


@login_required()
def edit_user_password_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = EditUserPasswordForm(request.POST, instance=request.user)

        if form.is_valid():
            form.change_password()
            return HttpResponseRedirect(reverse_lazy('user:profile_url'))
    else:
        form = EditUserPasswordForm(instance=request.user)

    return render(request, 'user/edit_user_password.html', {"form": form})