from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, DeleteView, CreateView
from catalog.models import CategoryModel, ProductModel
from catalog_administration.forms import UpdateCategoryForm
from mysite import settings
from django.urls import reverse_lazy


class StaffProfileRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        return super(StaffProfileRequiredMixin, self).dispatch(request, *args, **kwargs)


class CatalogAdministrationView(StaffProfileRequiredMixin, TemplateView):
    template_name = 'catalog_administration/models_list.html'






class CategoryListView(StaffProfileRequiredMixin, ListView):
    model = CategoryModel
    template_name = 'catalog_administration/category_list.html'


class CategoryDetailView(StaffProfileRequiredMixin, DetailView):
    model = CategoryModel
    template_name = 'catalog_administration/category_detail.html'
    slug_url_kwarg = 'category_slug'
    context_object_name = 'category'


class CategoryUpdateView(StaffProfileRequiredMixin, UpdateView):
    model = CategoryModel
    fields = '__all__'
    slug_url_kwarg = 'category_slug'
    template_name = 'catalog_administration/update.html'

    def get_success_url(self):
        return reverse_lazy('catalog_administration:category_detail_url',
                            kwargs={'category_slug': self.object.slug})


class CategoryDeleteView(StaffProfileRequiredMixin, DeleteView):
    model = CategoryModel
    template_name = 'catalog_administration/delete.html'
    slug_url_kwarg = 'category_slug'
    success_url = reverse_lazy('catalog_administration:category_list_url')


class CategoryCreateView(StaffProfileRequiredMixin, CreateView):
    model = CategoryModel
    template_name = 'catalog_administration/create.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('catalog_administration:category_detail_url',
                            kwargs={'category_slug': self.object.slug})







class ProductListView(StaffProfileRequiredMixin, ListView):
    model = ProductModel
    template_name = 'catalog_administration/product_list.html'


class ProductDetailView(StaffProfileRequiredMixin, DetailView):
    model = ProductModel
    template_name = 'catalog_administration/product_detail.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'


class ProductUpdateView(StaffProfileRequiredMixin, UpdateView):
    model = ProductModel
    template_name = 'catalog_administration/update.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('catalog_administration:product_detail_url',
                            kwargs={'product_slug': self.object.slug})


class ProductDeleteView(StaffProfileRequiredMixin, DetailView):
    model = ProductModel
    template_name = 'catalog_administration/delete.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'


class ProductCreateView(StaffProfileRequiredMixin, CreateView):
    model = ProductModel
    template_name = 'catalog_administration/create.html'
    slug_url_kwarg = 'product_slug'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('catalog_administration:product_detail_url',
                            kwargs={'product_slug': self.object.slug})
