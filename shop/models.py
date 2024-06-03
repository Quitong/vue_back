from django.db import models

# Create your models here.
class Goods(models.Model):
    category = models.ForeignKey("Category",models.CASCADE)
    name = models.CharField(max_length=50)
    cost = models.DecimalField("Цена",max_digits=20,decimal_places=2)

class Category(models.Model):
    name=models.CharField(max_length=50)