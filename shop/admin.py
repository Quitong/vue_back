from django.contrib import admin

from shop.models import Goods, Category

# Register your models here.
admin.site.register(Goods)
admin.site.register(Category)