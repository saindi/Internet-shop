from django.shortcuts import render
from django.views.generic import RedirectView, ListView, DetailView
from catalog.models import ProductModel, CategoryModel


class HomeView(RedirectView):
    pattern_name = 'catalog:catalog_url'


class CatalogView(ListView):
    model = CategoryModel
    template_name = 'catalog/catalog.html'
    context_object_name = 'categories'


class CategoryView(ListView):
    model = ProductModel
    template_name = 'catalog/category.html'
    context_object_name = 'products'
    allow_empty = False

    def get_queryset(self):
        return ProductModel.objects.filter(category__slug=self.kwargs['category_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = CategoryModel.objects.get(slug=self.kwargs['category_slug'])

        if "price_range" not in context:
            context["price_range"] = [0, 50000]

        return context

    def post(self, request, *args, **kwargs):
        price_range = request.POST.get('price_range').split(";")

        self.object_list = self.get_queryset().filter(price__range=price_range)

        return render(request, self.template_name, self.get_context_data(price_range=price_range))


class ProductView(DetailView):
    model = ProductModel
    slug_url_kwarg = 'product_slug'
    template_name = 'catalog/product.html'
    context_object_name = 'product'
