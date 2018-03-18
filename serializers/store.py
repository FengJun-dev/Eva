from api.models import Store
from rest_framework import serializers


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        models = Store
        fields = ('id',)