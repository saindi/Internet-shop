from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('<slug:product_slug>/', views.product_page),
]
