from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from user.models import User

import utils
from temp import current_user


def home_page(request: HttpRequest) -> HttpResponse:
    users = utils.get_users_dict(User.objects.all())

    return render(request, 'home.html', {"user_name": users[current_user]["username"]})
