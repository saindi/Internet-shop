from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def user_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'user/user.html')
