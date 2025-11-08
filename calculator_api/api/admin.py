# from django.contrib import admin

# # Register your models here.


from django.contrib import admin
from .models import CurrencyConversion

@admin.register(CurrencyConversion)
class CurrencyConversionAdmin(admin.ModelAdmin):
    list_display = ['id', 'from_currency', 'to_currency', 'amount', 'exchange_rate', 'result', 'success', 'created_at']
    list_filter = ['from_currency', 'to_currency', 'success', 'created_at']
    search_fields = ['from_currency', 'to_currency']

    def get_queryset(self, request):
        # Show conversion statistics
        return super().get_queryset(request)
