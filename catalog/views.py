from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from catalog.models import Product, Category
from user.models import User

from temp import current_user
import utils


def catalog_page(request: HttpRequest) -> HttpResponse:
    products = utils.get_products_dict(Product.objects.all())
    users = utils.get_users_dict(User.objects.all())
    categorys = utils.get_category_dict(Category.objects.all())

    return render(request, 'catalog.html', {"user_name": users[current_user]["username"],
                                            "products": products,
                                            "categorys": categorys})


def product_page(request: HttpRequest, product_slug: str) -> HttpResponse:
    products = utils.get_products_dict(Product.objects.all())
    users = utils.get_users_dict(User.objects.all())

    for product in products:
        if product_slug == product['slug']:
            return render(request, 'product.html', {"user_name": users[current_user]["username"],
                                                    "product": product})
    else:
        return render(request, 'no_page.html', {"user_name": users[current_user]["username"]})