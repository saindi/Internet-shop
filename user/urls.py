from django.urls import path
from user.views import user_view, signin_view, signup_view, logout_view, deactivation_user_view

urlpatterns = [
    path('user/', user_view, name="user_url"),
    path('user/deactivation/', deactivation_user_view, name="deactivation_user_url"),
    path('sign-in/', signin_view, name="signin_url"),
    path('sign-up/', signup_view, name="signup_url"),
    path('logout/', logout_view, name="logout_url"),
]
