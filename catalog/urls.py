from django.urls import path
from catalog.views import catalog_page, product_page, catalog_page_with_category

urlpatterns = [
    path('', catalog_page, name='catalog_url'),
    path('<slug:category_slug>/', catalog_page_with_category, name="catalog_page_with_category_url"),
    path('product/<slug:product_slug>/', product_page, name="product_url"),
]
