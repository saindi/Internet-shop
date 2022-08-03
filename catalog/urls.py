from django.urls import path
from catalog.views import catalog_page, product_page

urlpatterns = [
    path('', catalog_page, name='catalog_url'),
    path('<slug:product_slug>/', product_page),
]
