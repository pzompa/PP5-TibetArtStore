from django import template
from favorite.models import Favorite
from django.contrib.auth import get_user_model
from products.models import Product


register = template.Library()

@register.simple_tag

def is_favorited_by_user(product, user):
    if not product or not user:
        return False
    if not isinstance(product, Product) and not isinstance(product, int):
        try:
            product = int(product)
        except (ValueError, TypeError):
            return False
    if not isinstance(user, get_user_model()) and not isinstance(user, int):
        try:
            user = int(user)
        except (ValueError, TypeError):
            return False
    return Favorite.objects.filter(product=product, user=user).exists()
