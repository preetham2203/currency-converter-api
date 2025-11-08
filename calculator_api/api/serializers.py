# # api/serializers.py
# from rest_framework import serializers

# class AddNumbersSerializer(serializers.Serializer):
#     a = serializers.IntegerField(required=True)
#     b = serializers.IntegerField(required=True)

from rest_framework import serializers
from .models import CurrencyConversion

class CurrencyConversionSerializer(serializers.Serializer):
    from_currency = serializers.CharField(max_length=3, required=True)
    to_currency = serializers.CharField(max_length=3, required=True)
    amount = serializers.FloatField(default=1.0)

class CurrencyConversionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyConversion
        fields = ['id', 'from_currency', 'to_currency', 'amount', 'exchange_rate', 'result', 'success', 'created_at']