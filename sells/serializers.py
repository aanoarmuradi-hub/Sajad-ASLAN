from rest_framework import serializers
from .models import Sell

class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell
        fields = "__all__"
        