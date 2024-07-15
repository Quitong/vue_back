from django.contrib import admin

from shop.models import Goods, Category, BasketItem, UserLikes

# Register your models here.
admin.site.register(Goods)
admin.site.register(Category)
admin.site.register(BasketItem)
admin.site.register(UserLikes)