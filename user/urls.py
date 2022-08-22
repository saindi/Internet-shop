from django.urls import path
from django.conf import settings
from user.views import UserView, SignInView, SignUpView, DeactivationUserView, EditUserPasswordView, EditUserDataView
from django.contrib.auth.views import LogoutView

app_name = "user"

urlpatterns = [
    path('user/', UserView.as_view(), name="profile_url"),
    path('user/deactivation/', DeactivationUserView.as_view(), name="deactivation_url"),
    path('user/edit-data/', EditUserDataView.as_view(), name="edit_data_url"),
    path('user/edit-password/', EditUserPasswordView.as_view(), name="edit_password_url"),
    path(settings.LOGIN_URL[1:], SignInView.as_view(), name="signin_url"),
    path('sign-up/', SignUpView.as_view(), name="signup_url"),
    path('logout/', LogoutView.as_view(next_page='catalog:home_url'), name='logout_url'),
]
