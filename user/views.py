from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from user.models import UserModel

from temp import current_user_id, users


def user_page(request: HttpRequest) -> HttpResponse:
    # current_user = UserModel.objects.get(id=current_user_id)

    for user in users:
        if user["id"] == current_user_id:
            current_user = user

    context = {"user": current_user}

    return render(request, 'user/user.html', context)
