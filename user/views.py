from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from user.models import User

from temp import current_user
import utils


def user_page(request: HttpRequest) -> HttpResponse:
    users = utils.get_users_dict(User.objects.all())

    return render(request, 'user.html', {"user_name": users[current_user]["username"],
                                         "user_info": users[current_user]})