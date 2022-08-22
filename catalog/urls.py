from django.urls import path
from catalog.views import HomeView, CatalogView, CategoryView, CategoryUpdateView, CategoryDeleteView, \
    CategoryCreateView, ProductView, ProductUpdateView, ProductDeleteView, ProductCreateView


app_name = 'catalog'
urlpatterns = [
    path('', HomeView.as_view(), name='home_url'),

    path('catalog/', CatalogView.as_view(), name='catalog_url'),

    path('category/<slug:category_slug>/', CategoryView.as_view(), name="category_url"),
    path('category/<slug:category_slug>/update',CategoryUpdateView.as_view(), name="category_update_url"),
    path('category/<slug:category_slug>/delete', CategoryDeleteView.as_view(), name="category_delete_url"),
    path('category/create', CategoryCreateView.as_view(), name="category_create_url"),

    path('product/<slug:product_slug>/', ProductView.as_view(), name="product_url"),
    path('product/<slug:product_slug>/update', ProductUpdateView.as_view(), name="product_update_url"),
    path('product/<slug:product_slug>/delete', ProductDeleteView.as_view(), name="product_delete_url"),
    path('product/create', ProductCreateView.as_view(), name="product_create_url"),




    # path('staff/', CatalogAdministrationView.as_view(), name="staff_catalog_url"),
    #
    # path('staff/category/', CategoryListView.as_view(), name="staff_category_list_url"),
    # path('staff/category/detail/<slug:category_slug>/', CategoryDetailView.as_view(), name="staff_category_detail_url"),
    # path('staff/category/update/<slug:category_slug>/', CategoryUpdateView.as_view(), name="staff_category_update_url"),
    # path('staff/category/delete/<slug:category_slug>/', CategoryDeleteView.as_view(), name="staff_category_delete_url"),
    # path('staff/category/create/', CategoryCreateView.as_view(), name="staff_category_create_url"),
    #
    #
    #
]