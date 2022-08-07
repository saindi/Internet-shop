from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User


def user_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_anonymous:
        return HttpResponseRedirect(reverse_lazy('signin_url'))

    return render(request, 'user/user.html')


def signin_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('user_url'))

    if request.method == "POST":
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])

        if user is None:
            return HttpResponseRedirect(reverse_lazy('signin_url'))

        login(request, user)

        return HttpResponseRedirect(reverse_lazy('home_url'))

    return render(request, 'user/signin.html')


def signup_view(request: HttpRequest) -> HttpResponse:
    #
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('user_url'))

    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2 and len(User.objects.filter(username=username)) == 0:
            User.objects.create_user(username=username,
                                     password=password1)
            return HttpResponseRedirect(reverse_lazy('signin_url'))

        return HttpResponseRedirect(reverse_lazy('signup_url'))

    return render(request, 'user/signup.html')


def logout_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_anonymous:
        return HttpResponseRedirect(reverse_lazy('home_url'))

    logout(request)
    return HttpResponseRedirect(reverse_lazy('home_url'))


def deactivation_user_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_anonymous:
        return HttpResponseRedirect(reverse_lazy('home_url'))

    user = User.objects.get(username=request.user.username)

    user.is_active = False
    user.save()

    logout(request)

    return HttpResponseRedirect(reverse_lazy('home_url'))