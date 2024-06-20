# serializers.py
from rest_framework.serializers import ModelSerializer

from shop.models import Goods, Basket


class GoodsSerializer(ModelSerializer):
    class Meta():
        model = Goods
        fields = ['name', 'cost','likes']


class BasketSerializer(ModelSerializer):
    class Meta():
        model=Basket
        fields = ['user']