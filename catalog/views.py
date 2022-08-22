from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, DeleteView, CreateView, RedirectView
from catalog.models import CategoryModel, ProductModel
from mysite import settings
from django.urls import reverse_lazy


class StaffProfileRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        return super(StaffProfileRequiredMixin, self).dispatch(request, *args, **kwargs)


class HomeView(RedirectView):
    pattern_name = 'catalog:catalog_url'


class CatalogView(ListView):
    model = CategoryModel
    template_name = 'catalog/catalog.html'
    context_object_name = 'categories'


class CategoryUpdateView(StaffProfileRequiredMixin, UpdateView):
    model = CategoryModel
    fields = '__all__'
    slug_url_kwarg = 'category_slug'
    template_name = 'catalog/update.html'


class CategoryDeleteView(StaffProfileRequiredMixin, DeleteView):
    model = CategoryModel
    template_name = 'catalog/delete.html'
    slug_url_kwarg = 'category_slug'
    success_url = '/'


class CategoryCreateView(StaffProfileRequiredMixin, CreateView):
    model = CategoryModel
    template_name = 'catalog/create.html'
    fields = '__all__'


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


class ProductUpdateView(StaffProfileRequiredMixin, UpdateView):
    model = ProductModel
    template_name = 'catalog/update.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'
    fields = '__all__'


class ProductDeleteView(StaffProfileRequiredMixin, DeleteView):
    model = ProductModel
    template_name = 'catalog/delete.html'
    slug_url_kwarg = 'product_slug'
    success_url = reverse_lazy('catalog:home_url')


class ProductCreateView(StaffProfileRequiredMixin, CreateView):
    model = ProductModel
    template_name = 'catalog/create.html'
    slug_url_kwarg = 'product_slug'
    fields = '__all__'

