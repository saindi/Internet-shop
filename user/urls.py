from django.urls import path
from user.views import user_view

urlpatterns = [
    path('user/', user_view, name="user_url"),
]
