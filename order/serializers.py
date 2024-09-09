from rest_framework import serializers
from .models import Order,OrderItem,ShippingAdress

#1 OrderItemSerializer
class OrderItemSerializer(serializers.ModelSerializer):
    # productt بدل استخدام product مشكلة عدم وجود الاسم عند كريت اورد ايتم جديد  
    def get_productt(seelf,obj):
        return obj.product.name 
    productt = serializers.SerializerMethodField()


    count_stock = serializers.SerializerMethodField()
    def get_count_stock(seelf,obj):
        quantity = obj.quantity
        count_stock = obj.product.count_stock
        return count_stock - quantity
   
    class Meta:
        model = OrderItem
        fields= '__all__'

# 2 ShippingAdressSerializer
class ShippingAdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAdress
        fields= '__all__'
        
# OrderSerializer
class OrderSerializer(serializers.ModelSerializer):

    orderitems = serializers.SerializerMethodField()
    def get_orderitems(seelf,obj):
        orderitems = obj.orderitem_order.all()
        serializer = OrderItemSerializer(orderitems,many=True)
        return serializer.data
    
    shipping_address = serializers.SerializerMethodField()
    def get_shipping_address(seelf,obj):
        if hasattr(obj,'shippingsdress_order'):
            address = obj.shippingsdress_order
            serializer = ShippingAdressSerializer(address)
            return serializer.data
        else:
            return {}
    
    class Meta:
        model = Order
        fields= '__all__'