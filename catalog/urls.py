from django.urls import path
from catalog.views import home_view, catalog_view, product_view, category_view

urlpatterns = [
    path('', home_view, name='home_url'),
    path('catalog/', catalog_view, name='catalog_url'),
    path('catalog/<slug:category_slug>/', category_view, name="category_url"),
    path('catalog/<slug:category_slug>/<slug:product_slug>/', product_view, name="product_url"),
]
