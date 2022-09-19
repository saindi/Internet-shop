from django.urls import path
from catalog.views import (
    HomeView,
    CategoryListView,
    ProductListView,
    CategoryUpdateView,
    CategoryDeleteView,
    CategoryCreateView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
    ProductCreateView,
    StaffCategoryListView,
    StaffProductListView,
)


app_name = 'catalog'

urlpatterns = [
    path('', HomeView.as_view(), name='home_url'),

    path('category/', CategoryListView.as_view(), name='category_list_url'),
    path('category/create/', CategoryCreateView.as_view(), name="category_create_url"),
    path('category/<slug:category_slug>/update/', CategoryUpdateView.as_view(), name="category_update_url"),
    path('category/<slug:category_slug>/delete/', CategoryDeleteView.as_view(), name="category_delete_url"),

    path('product/create/', ProductCreateView.as_view(), name="product_create_url"),
    path('category/<slug:category_slug>/', ProductListView.as_view(), name="product_list_url"),
    path('product/<slug:product_slug>/', ProductDetailView.as_view(), name="product_detail_url"),
    path('product/<slug:product_slug>/update/', ProductUpdateView.as_view(), name="product_update_url"),
    path('product/<slug:product_slug>/delete/', ProductDeleteView.as_view(), name="product_delete_url"),


    path('staff/category/', StaffCategoryListView.as_view(), name="staff_category_list_url"),
    path('staff/product/', StaffProductListView.as_view(), name="staff_product_delete_url"),
]
