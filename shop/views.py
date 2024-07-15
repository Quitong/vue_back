from django.http import Http404
from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from shop.models import Goods, Category, BasketItem, Basket, UserLikes
from shop.serializers import GoodsSerializer, BasketSerializer
from shop.utils import get_client_ip


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
        user = request.user
        if user.is_anonymous:
            ip = get_client_ip(request)
            if UserLikes.objects.filter(good=tovar,ip=ip).exists():
                return Response({'status': 'you already liked'}, status=208)
            user_like = UserLikes(good=tovar,ip=ip)
        else:
            if UserLikes.objects.filter(good=tovar,user=user).exists():
                return Response({'status': 'you already liked'},status=208)
            user_like = UserLikes(good=tovar,user=user)

        user_like.save()
        tovar.likes += 1
        tovar.save()
        return Response({'status': 'ok'})
    @action(detail=True, methods=['post'])
    def add_to_basket(self, request, pk=None):
        qs = self.get_queryset()
        tovar = qs.filter(pk=pk).first()
        user = request.user
        basket = user.baskets.last()
        if basket is None:
            basket = Basket(user=user)
            basket.save()
        b_item = BasketItem.objects.filter(
            basket=basket,
            good=tovar,
        ).first()
        if b_item is None: #у нас нет такого в корзине
            BasketItem(
                basket=basket,
                good = tovar,
                kolvo = 1
            ).save()
        else:
            b_item.kolvo+=1
            b_item.save()
        return Response({'status': 'ok'},status=208)


class BasketViewSet(GenericViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    def _retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    def get_object(self):
        user = self.request.user
        basket = user.baskets.last()
        return basket
    def list(self, request, *args, **kwargs):
        return self._retrieve(request, *args, **kwargs)

