from django.http import HttpResponse
from csvprocessor.models import Product
from django.db import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache



@csrf_exempt
def product_analysis(request):
    if request.method == 'GET':

        try:

            query_params = request.GET
            category = query_params.get('category',"").strip().lower()
            min_price = query_params.get('min_price')
            max_price = query_params.get('max_price')

            if not category or not min_price or not max_price:
                return JsonResponse({'error': 'Category, min_price, and max_price parameters are required'}, status=400)
            
            #check for cache  data
            cached_response = cache.get(f'product_analysis_{category}_{min_price}_{max_price}')
            if cached_response:
                return JsonResponse(cached_response)

            products = Product.objects.filter(category__iexact=category, price__gte=min_price, price__lte=max_price)

            total_products = products.count()
            print(total_products)
            average_price = products.aggregate(models.Avg('price'))['price__avg'] if total_products > 0 else 0
            total_stock_value = products.aggregate(total_value = models.Sum(models.F('stock') * models.F('price')))['total_value'] if total_products > 0 else 0


            response = {
                'total_products': total_products,
                'average_price': average_price,
                'total_stock_value': total_stock_value,
            }

    
            cache.set(f'product_analysis_{category}_{min_price}_{max_price}', response, 600)

            return JsonResponse(response)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    else:
        return HttpResponse('Method not allowed', status=405)





