from django.db.models import Sum
from rest_framework import viewsets
from django.shortcuts import render
from .models import Order
from .serializers import OrderSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

@csrf_exempt
def delete_order(request, order_id):
    if request.method == "DELETE":
        try:
            order = Order.objects.get(id=order_id)
            order.delete()
            return JsonResponse({"message": "Order deleted"}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({"error": "Order not found"}, status=404)
    return JsonResponse({"error": "Invalid request method"}, status=400)

def revenue_view(request):
    revenue = Order.objects.filter(status="оплачено").aggregate(total_revenue=Sum("total_price"))["total_revenue"] or 0
    return render(request, "orders/revenue.html", {"revenue": revenue})