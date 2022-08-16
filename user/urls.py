from django.urls import path
from user.views import user_view, signin_view, signup_view, logout_view, deactivation_user_view, edit_user_data_view, \
    edit_user_password_view

app_name = "user"
urlpatterns = [
    path('user/', user_view, name="profile_url"),
    path('user/deactivation/', deactivation_user_view, name="deactivation_url"),
    path('user/edit-data/', edit_user_data_view, name="edit_data_url"),
    path('user/edit-password/', edit_user_password_view, name="edit_password_url"),
    path('sign-in/', signin_view, name="signin_url"),
    path('sign-up/', signup_view, name="signup_url"),
    path('logout/', logout_view, name="logout_url"),
]
