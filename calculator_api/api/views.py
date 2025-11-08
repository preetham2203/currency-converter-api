from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json
from .models import CurrencyConversion
from .serializers import CurrencyConversionSerializer, CurrencyConversionResponseSerializer

@api_view(['POST'])
def convert_currency(request):
    """
    Convert currency using multiple FREE APIs with fallback to mock data
    """
    serializer = CurrencyConversionSerializer(data=request.data)
    
    if serializer.is_valid():
        from_currency = serializer.validated_data['from_currency'].upper()
        to_currency = serializer.validated_data['to_currency'].upper()
        amount = serializer.validated_data['amount']

        # Mock exchange rates as fallback
        mock_rates = {
            'USD': {'INR': 83.25, 'EUR': 0.92, 'GBP': 0.79, 'JPY': 148.50},
            'EUR': {'USD': 1.09, 'INR': 90.50, 'GBP': 0.86, 'JPY': 161.20},
            'GBP': {'USD': 1.27, 'EUR': 1.16, 'INR': 105.30, 'JPY': 187.90},
            'INR': {'USD': 0.012, 'EUR': 0.011, 'GBP': 0.0095, 'JPY': 1.78},
        }

        # Try multiple FREE APIs
        free_apis = [
            {
                'name': 'Frankfurter',
                'url': f"https://api.frankfurter.app/latest?from={from_currency}&to={to_currency}",
                'parser': lambda data: data.get('rates', {}).get(to_currency)
            },
            {
                'name': 'ExchangeRate-API', 
                'url': f"https://open.er-api.com/v6/latest/{from_currency}",
                'parser': lambda data: data.get('rates', {}).get(to_currency) if data.get('result') == 'success' else None
            },
            {
                'name': 'FastForex (Demo)',
                'url': f"https://api.fastforex.io/fetch-one?from={from_currency}&to={to_currency}&api_key=demo",
                'parser': lambda data: data.get('result', {}).get(to_currency)
            }
        ]

        use_real_api = False
        real_api_data = None
        api_used = None
        
        for api in free_apis:
            print(f"🔄 Trying {api['name']} API: {api['url']}")
            
            try:
                response = requests.get(api['url'], timeout=8)  # Increased timeout
                data = response.json()
                
                if response.status_code == 200:
                    rate = api['parser'](data)
                    if rate:
                        use_real_api = True
                        real_api_data = {
                            'rate': rate,
                            'result': amount * rate
                        }
                        api_used = api['name']
                        print(f"✅ {api['name']} API call successful - Rate: {rate}")
                        break
                    else:
                        print(f"❌ {api['name']} API rate not found")
                else:
                    print(f"❌ {api['name']} API failed with status: {response.status_code}")
                    
            except requests.exceptions.Timeout:
                print(f"⏰ {api['name']} API timeout")
                continue
            except requests.exceptions.ConnectionError:
                print(f"🔌 {api['name']} API connection error")
                continue
            except Exception as e:
                print(f"❌ {api['name']} API error: {e}")
                continue

        # Use real API data if successful, otherwise use mock data
        if use_real_api and real_api_data:
            rate = real_api_data['rate']
            result = real_api_data['result']
            success = True
            data_source = f"FREE API ({api_used})"
        else:
            # Use mock data as fallback
            rate = mock_rates.get(from_currency, {}).get(to_currency)
            result = amount * rate if rate else None
            success = bool(rate)
            data_source = "mock data (all APIs failed)"
            
            print(f"🔄 Using {data_source}: {from_currency}->{to_currency} = {rate}")

        if success and rate:
            # Store successful conversion in database
            conversion = CurrencyConversion.objects.create(
                from_currency=from_currency,
                to_currency=to_currency,
                amount=amount,
                exchange_rate=rate,
                result=result,
                success=True
            )

            response_data = {
                "motd": {
                    "msg": "Real-time rates provided by FREE APIs",
                    "url": "https://www.frankfurter.app/"
                },
                "success": True,
                "query": {
                    "from": from_currency,
                    "to": to_currency,
                    "amount": amount
                },
                "info": {
                    "rate": rate,
                    "source": api_used if use_real_api else "Mock Data"
                },
                "result": result,
                "conversion_id": conversion.id,
                "data_source": data_source
            }

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            # Conversion failed
            conversion = CurrencyConversion.objects.create(
                from_currency=from_currency,
                to_currency=to_currency,
                amount=amount,
                exchange_rate=0,
                result=0,
                success=False
            )

            return Response({
                "motd": {
                    "msg": "Real-time rates provided by FREE APIs",
                    "url": "https://www.frankfurter.app/"
                },
                "success": False,
                "query": {
                    "from": from_currency,
                    "to": to_currency,
                    "amount": amount
                },
                "info": {
                    "rate": None
                },
                "result": None,
                "conversion_id": conversion.id,
                "error": f"Conversion rate not available for {from_currency} to {to_currency}"
            }, status=status.HTTP_400_BAD_REQUEST)

    return Response({
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_conversion_history(request):
    """
    Get all conversion history from database
    """
    conversions = CurrencyConversion.objects.all().order_by('-created_at')
    serializer = CurrencyConversionResponseSerializer(conversions, many=True)
    
    return Response({
        "success": True,
        "count": conversions.count(),
        "data": serializer.data
    })


@api_view(['GET'])
def get_conversion_by_id(request, conversion_id):
    """
    Get specific conversion by ID
    """
    try:
        conversion = CurrencyConversion.objects.get(id=conversion_id)
        serializer = CurrencyConversionResponseSerializer(conversion)
        
        return Response({
            "success": True,
            "data": serializer.data
        })
    except CurrencyConversion.DoesNotExist:
        return Response({
            "success": False,
            "error": "Conversion not found"
        }, status=status.HTTP_404_NOT_FOUND)