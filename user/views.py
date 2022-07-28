from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from temp import users, current_user


def user_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'user.html', {"user_name": users[current_user]["username"],
                                         "user_info": users[current_user]})