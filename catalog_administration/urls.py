from django.urls import path
from catalog_administration.views import CatalogAdministrationView, CategoryListView, CategoryDetailView, \
    CategoryUpdateView, CategoryDeleteView, CategoryCreateView, ProductListView, ProductDetailView,  ProductUpdateView, \
    ProductDeleteView, ProductCreateView

app_name = "catalog_administration"

urlpatterns = [
    path('catalog_administration/', CatalogAdministrationView.as_view(), name="catalog_administration_url"),

    path('catalog_administration/category/', CategoryListView.as_view(), name="category_list_url"),
    path('catalog_administration/category/detail/<slug:category_slug>/', CategoryDetailView.as_view(), name="category_detail_url"),
    path('catalog_administration/category/update/<slug:category_slug>/', CategoryUpdateView.as_view(), name="category_update_url"),
    path('catalog_administration/category/delete/<slug:category_slug>/', CategoryDeleteView.as_view(), name="category_delete_url"),
    path('catalog_administration/category/create/', CategoryCreateView.as_view(), name="category_create_url"),

    path('catalog_administration/product/', ProductListView.as_view(), name="product_list_url"),
    path('catalog_administration/product/detail/<slug:product_slug>/', ProductDetailView.as_view(), name="product_detail_url"),
    path('catalog_administration/product/update/<slug:product_slug>/', ProductUpdateView.as_view(), name="product_update_url"),
    path('catalog_administration/product/delete/<slug:product_slug>/', ProductDeleteView.as_view(), name="product_delete_url"),
    path('catalog_administration/product/create/', ProductCreateView.as_view(), name="product_create_url"),
]