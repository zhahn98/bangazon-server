from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import Order, Item, OrderItem

class OrderView(ViewSet):
  def retrieve(self, request, pk):

    try:
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    except order.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

  def list(self, request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

  def create(self, request):
    """Handles POST order"""
    
    item_ids = request.data.get("items", [])
    
    order = Order.objects.create(
        order_name=request.data["order_name"],
        customer_name=request.data["customer_name"],
        phone_number=request.data["phone_number"],
        email=request.data["email"],
        order_type=request.data["order_type"],
        payment_type=request.data["payment_type"],
        tip=request.data["tip"],
        order_total=request.data["order_total"]
    )

    for item_id in item_ids:
        item = Item.objects.get(id=item_id)
        OrderItem.objects.create(order=order, item=item)

    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
      order = Order.objects.get(pk=pk)
      order.order_name = request.data["order_name"]
      order.customer_name = request.data["customer_name"]
      order.phone_number = request.data["phone_number"]
      order.email = request.data["email"]
      order.order_type = request.data["order_type"]
      order.payment_type = request.data["payment_type"]
      order.tip = request.data["tip"]
      order.order_total = request.data["order_total"]
      order.items.set(request.data["items"])
      
      order.save()

      return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):

      order = Order.objects.get(pk=pk)
      order.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)

class OrderSerializer(serializers.ModelSerializer):  
  """Order JSON serializer"""
  
  class Meta:
    model = Order
    fields = ('id', 'order_name', 'customer_name', 'completion_status', 'phone_number', 'email', 'order_type', 'payment_type', 'date', 'user_id', 'tip', 'order_total', 'items')
