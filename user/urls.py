from django.urls import path
from user.views import user_page

urlpatterns = [
    path('', user_page, name="user_page"),
]
