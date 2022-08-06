from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from catalog.models import ProductModel, CategoryModel


def catalog_page(request: HttpRequest) -> HttpResponse:

    products = ProductModel.objects.all()
    categorys = CategoryModel.objects.all()

    context = {"products": products,
               "categorys": categorys}

    return render(request, 'catalog/catalog.html', context)


def catalog_page_with_category(request: HttpRequest, category_slug: str) -> HttpResponse:
    products = ProductModel.objects.filter(category_id=category_slug)
    categorys = CategoryModel.objects.all()

    context = {"products": products,
               "categorys": categorys}

    categorys_slug = []
    for category in categorys:
        categorys_slug.append(category.slug)

    if category_slug not in categorys_slug:
        return render(request, 'no_page.html', context)

    return render(request, 'catalog/catalog.html', context)


def product_page(request: HttpRequest, product_slug: str) -> HttpResponse:
    try:
        product = ProductModel.objects.get(slug=product_slug)

        context = {"product": product}

        return render(request, 'catalog/product.html', context)
    except ProductModel.DoesNotExist:

        return render(request, 'no_page.html')