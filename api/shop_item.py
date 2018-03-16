from api.models import ShopItem
from serializers.shop_item import ShopItemSerializer
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response


class ShopItemViewSet(viewsets.ModelViewSet):
    queryset = ShopItem.objects.all()
    serializer_class = ShopItemSerializer