from user.models import User
from catalog.models import Product, Category


def get_users_dict(all_users: User) -> list:
    users = []

    for user in all_users:
        temp_dict = {}

        temp_dict["id"] = user.id
        temp_dict["username"] = user.username
        temp_dict["first_name"] = user.first_name
        temp_dict["last_name"] = user.last_name

        users.append(temp_dict)

    return users


def get_products_dict(all_product: Product) -> list:
    products = []

    for product in all_product:
        temp_dict = {}

        temp_dict["slug"] = product.slug
        temp_dict["name"] = product.name
        temp_dict["available"] = product.available
        temp_dict["description"] = product.description
        temp_dict["price"] = product.price
        temp_dict["category_id"] = product.category_id
        temp_dict["img"] = product.img

        products.append(temp_dict)

    return products


def get_category_dict(all_category: Product) -> list:
    categorys = []

    for category in all_category:
        temp_dict = {}

        temp_dict["slug"] = category.slug
        temp_dict["name"] = category.name
        temp_dict["description"] = category.description

        categorys.append(temp_dict)

    return categorys

