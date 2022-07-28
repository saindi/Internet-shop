from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from temp import users, current_user, products


def homepage(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html', {"user_name": users[current_user]["username"],
                                         "products": products})


def product_page(request: HttpRequest, product_slug: str) -> HttpResponse:
    for user_dict in products:
        if product_slug == user_dict['slug']:
            return render(request, 'product.html', {"user_name": users[current_user]["username"],
                                                    "product_info": user_dict})
    else:
        return render(request, 'no_page.html', {"user_name": users[current_user]["username"]})