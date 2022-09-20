from rest_framework import serializers
from catalog.models import CategoryModel, ProductModel


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"


class CategorySerializers(serializers.ModelSerializer):
    products = ProductSerializers(many=True)

    class Meta:
        model = CategoryModel
        fields = "__all__"
