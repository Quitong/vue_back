from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
User = get_user_model()
# Create your models here.
class Goods(models.Model):
    category = models.ForeignKey("Category",models.CASCADE)
    name = models.CharField(max_length=50)
    cost = models.DecimalField("Цена",max_digits=20,decimal_places=2)
    likes = models.IntegerField(default=0)

class Category(models.Model):
    name=models.CharField(max_length=50)

class Basket(models.Model):
    user = models.ForeignKey(User, models.CASCADE, related_name="baskets")


def validate_kolvo(value):
   if value < 0:
        raise ValidationError(
          "kolvo is wrong and not good, you should be ashamed"
        )

class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, models.CASCADE, related_name="basket_items")
    good = models.ForeignKey(Goods, models.CASCADE)
    kolvo = models.IntegerField(validators=[validate_kolvo,])