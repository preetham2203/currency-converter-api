from django.db import models

class CurrencyConversion(models.Model):
    from_currency = models.CharField(max_length=3)
    to_currency = models.CharField(max_length=3)
    amount = models.FloatField(default=1.0)
    exchange_rate = models.FloatField()
    result = models.FloatField()
    success = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_currency} to {self.to_currency} - {self.result}"