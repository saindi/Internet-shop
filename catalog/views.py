from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.models import ProductModel, CategoryModel
from mysite.views import page_not_found_view


def home_view(request: HttpRequest) -> HttpResponse:
    return HttpResponseRedirect(reverse_lazy('catalog_url'))


def catalog_view(request: HttpRequest) -> HttpResponse:
    context = {"categorys": CategoryModel.objects.all()}

    return render(request, 'catalog/catalog.html', context)


def category_view(request: HttpRequest, category_slug: str) -> HttpResponse:
    if len(request.GET) != 0:
        price_range = request.GET['price_interval'].split(";")

        products = ProductModel.objects.filter(category_id=category_slug, price__range=price_range)
    else:
        products = ProductModel.objects.filter(category_id=category_slug)

    try:
        category = CategoryModel.objects.get(slug=category_slug)
    except CategoryModel.DoesNotExist as err:
        return page_not_found_view(request, err)

    context = {"products": products,
               "category": category}

    return render(request, 'catalog/category.html', context)


def product_view(request: HttpRequest, category_slug: str, product_slug: str) -> HttpResponse:
    try:
        product = ProductModel.objects.get(slug=product_slug)
        category = CategoryModel.objects.get(slug=category_slug)

    except ProductModel.DoesNotExist as err:
        return page_not_found_view(request, err)

    except CategoryModel.DoesNotExist as err:
        return page_not_found_view(request, err)

    context = {"product": product}

    return render(request, 'catalog/product.html', context)