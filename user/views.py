from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from mysite import settings
from user.forms import SignUpForm, SignInForm, EditUserDataForm, EditUserPasswordForm
from user.models import UserModel

from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView


class WithoutLoginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        return super(WithoutLoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class UserView(LoginRequiredMixin, TemplateView):
    template_name = 'user/user.html'


class SignInView(WithoutLoginRequiredMixin, LoginView):
    template_name = 'user/signin.html'
    form_class = SignInForm


class SignUpView(WithoutLoginRequiredMixin, CreateView):
    model = UserModel
    template_name = 'user/signup.html'
    form_class = SignUpForm

    def get_success_url(self):
        return reverse_lazy('user:signin_url')


class EditUserDataView(LoginRequiredMixin, UpdateView):
    model = UserModel
    form_class = EditUserDataForm
    template_name = 'user/edit_user_data.html'

    def get_object(self, **kwargs):
        return self.request.user


class EditUserPasswordView(LoginRequiredMixin, UpdateView):
    model = UserModel
    form_class = EditUserPasswordForm
    template_name = 'user/edit_user_password.html'

    def get_object(self, **kwargs):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('user:signin_url')


class DeactivationUserView(LoginRequiredMixin, DeleteView):
    model = UserModel
    template_name = 'user/deactivation_user.html'

    def get_object(self, **kwargs):
        return self.request.user

    def form_valid(self, form):
        self.object.is_active = False
        self.object.save()

        logout(self.request)

        return HttpResponseRedirect(reverse_lazy('catalog:home_url'))
