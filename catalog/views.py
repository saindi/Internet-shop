from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from catalog.models import ProductModel, CategoryModel
from user.models import UserModel

from temp import current_user_id


def catalog_page(request: HttpRequest) -> HttpResponse:
    current_user = UserModel.objects.get(id=current_user_id)
    products = ProductModel.objects.all()
    categorys = CategoryModel.objects.all()

    context = {"user": current_user,
               "products": products,
               "categorys": categorys}

    return render(request, 'catalog.html', context)


def product_page(request: HttpRequest, product_slug: str) -> HttpResponse:
    try:
        current_user = UserModel.objects.get(id=current_user_id)
        product = ProductModel.objects.get(slug=product_slug)

        context = {"user": current_user,
                   "product": product}

        return render(request, 'product.html', context)
    except ProductModel.DoesNotExist:
        current_user = UserModel.objects.get(id=current_user_id)

        context = {"user": current_user}

        return render(request, 'no_page.html', context)