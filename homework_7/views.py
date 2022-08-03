from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from user.models import UserModel

from temp import current_user_id


def home_page(request: HttpRequest) -> HttpResponse:
    user = UserModel.objects.get(id=current_user_id)

    context = {"user": user}

    return render(request, 'home.html', context)
