from django.contrib import admin
from catalog.models import ProductModel, CategoryModel


class ProductModelAdmin(admin.ModelAdmin):
    list_display = "slug", "name", "category_id", "amount", "available"
    list_editable = "amount", "available"
    list_filter = "category_id", "amount", "price"
    prepopulated_fields = {
        "slug": ["name"],
    }


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = "slug", "name", "description"
    prepopulated_fields = {
        "slug": ["name"],
    }

admin.site.register(ProductModel, ProductModelAdmin)
admin.site.register(CategoryModel, CategoryModelAdmin)