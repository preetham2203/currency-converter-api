# from django.urls import path
# from . import views

# urlpatterns = [
#     path('add/', views.add_numbers, name='add_numbers'),
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     # Currency conversion endpoints
#     path('convert/', views.convert_currency, name='convert_currency'),
#     path('history/', views.get_conversion_history, name='conversion_history'),
#     path('history/<int:conversion_id>/', views.get_conversion_by_id, name='conversion_by_id'),
    
#     # Original addition endpoint
#     path('add/', views.add_numbers, name='add_numbers'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('convert/', views.convert_currency, name='convert_currency'),
    path('history/', views.get_conversion_history, name='conversion_history'),
    path('history/<int:conversion_id>/', views.get_conversion_by_id, name='conversion_by_id'),
    # path('add/', views.add_numbers, name='add_numbers'),
]