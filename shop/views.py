from django.http import Http404
from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from shop.models import Goods, Category
from shop.serializers import GoodsSerializer


#'shop/goods/<int:cat_id>/<int:goods_id>/'
# Create your views here.

def cat_goods_view(request,cat_id,goods_id):

    qs = Goods.objects.filter(id=goods_id,category__id=cat_id)
    if not qs.exists():
        raise Http404
    good = qs.first()
    return render(
        request,
        'cat_gooods.html',
        {
            'good' : good,
        }
    )
    # Goods.objects.filter(name="Перекись",category__id=2)

class GoodsViewSet(ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    def perform_create(self, serializer):
        a = Goods(name=serializer.data['name'],
                  cost=serializer.data['cost'])
        a.category = Category.objects.first()
        a.save()
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        qs = self.get_queryset()
        tovar = qs.filter(pk=pk).first()
        tovar.likes += 1
        tovar.save()
        return Response({'status': 'ok'})


