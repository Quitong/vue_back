# serializers.py
from rest_framework.serializers import ModelSerializer

from shop.models import Goods


class GoodsSerializer(ModelSerializer):
    class Meta():
        model = Goods
        fields = ['name', 'cost','likes']