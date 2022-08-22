from django import forms
from django.core.exceptions import ValidationError

from catalog.models import CategoryModel, ProductModel


class UpdateCategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = '__all__'

    def clean_slug(self):
        slug = self.cleaned_data["slug"]

        if self.instance.slug == slug:
            return slug

        try:
            CategoryModel.objects.get(slug=slug)
            raise ValidationError("Користувач із таким ім'ям вже є")
        except CategoryModel.DoesNotExist:
            return slug
