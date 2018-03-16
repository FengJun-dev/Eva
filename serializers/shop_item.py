from rest_framework import serializers
from api.models import ShopItem


class ShopItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShopItem
        fields = ('id', 'item_name', 'store', 'created', 'like', 'category', 'sub_category', 'region', 'price', 'stock')
