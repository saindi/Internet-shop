from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

from user.models import UserModel


class SignInForm(forms.Form):
    username = forms.CharField(label=False,
                               widget=forms.TextInput(attrs={"class": "form-control",
                                                             "placeholder": "Username"}))

    password = forms.CharField(label=False,
                               widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                 "placeholder": "Password"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]

        self.user = authenticate(username=username, password=password)

        if self.user is None:
            raise ValidationError("Неправильне ім'я користувача або пароль")


class SignUpForm(forms.Form):
    username = forms.CharField(label=False,
                               widget=forms.TextInput(attrs={"class": "form-control",
                                                             "placeholder": "Username"}))

    email = forms.CharField(label=False,
                            widget=forms.EmailInput(attrs={"class": "form-control",
                                                           "placeholder": "Email"}))

    password1 = forms.CharField(label=False,
                                widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                  "placeholder": "Password"}))

    password2 = forms.CharField(label=False,
                                widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                  "placeholder": "Confirm password"}))

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            UserModel.objects.get(username=username)
            raise ValidationError("Користувач із таким ім'ям вже є")
        except UserModel.DoesNotExist:
            return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            UserModel.objects.get(email=email)
            raise ValidationError("Користувач із такою поштою вже є")
        except UserModel.DoesNotExist:
            return email

    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise ValidationError("Паролі не однакові")

    def create_user(self):
        username = self.cleaned_data["username"]
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password1"]

        UserModel.objects.create_user(username=username,
                                      email=email,
                                      password=password)


class EditUserDataForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    first_name = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))

    last_name = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={"class": "form-control"}))

    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'email', 'img']


class EditUserPasswordForm(forms.ModelForm):
    password = forms.CharField(label=False,
                               widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                 "placeholder": "password",
                                                                 "value": ""}))
    password2 = forms.CharField(label=False,
                                widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                  "placeholder": "Confirm password"}))

    class Meta:
        model = UserModel
        fields = ['password']

    def clean(self):
        password = self.cleaned_data["password"]
        password2 = self.cleaned_data["password2"]

        if password != password2:
            raise ValidationError("Паролі не однакові")

    def change_password(self):
        self.instance.set_password(self.cleaned_data["password"])
        self.instance.save()
