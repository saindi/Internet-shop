from django.urls import path
from catalog.views import HomeView, CatalogView, CategoryView, ProductView


app_name = 'catalog'
urlpatterns = [
    path('', HomeView.as_view(), name='home_url'),
    path('catalog/', CatalogView.as_view(), name='catalog_url'),
    path('category/<slug:category_slug>/', CategoryView.as_view(), name="category_url"),
    path('product/<slug:product_slug>/', ProductView.as_view(), name="product_url"),
]
