from django.urls import path
from catalog.views import home_page, product_page

urlpatterns = [
    path('', home_page, name="homepage"),
    path('<slug:product_slug>/', product_page),
]
