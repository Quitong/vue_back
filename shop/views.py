from django.http import Http404
from django.shortcuts import render, redirect
from django.views.defaults import page_not_found

from shop.models import Goods
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
