from django.shortcuts import render
from .serializers import OrderSerializer,OrderItemSerializer,ShippingAdressSerializer
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser,BasePermission
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Order,OrderItem,ShippingAdress
from django.utils import timezone
from datetime import datetime
# Create your views here.

# 1 addOrder --- addOrderItems ---  ShippingAddress

# *** create order 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    try :
        print('user create order is==',request.user)
        data = request.data
        serializer = OrderSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex :
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)
    
# ***  create orderitem 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_orderitem(request):
    try :
        print('user create_ orderitem  is==',request.user)
        data = request.data
        print('dataaaaaa===',data)
        if OrderItem.objects.filter(product_id = data['product']).exists() == False:
            serializer = OrderItemSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else :
            return Response({'message':'this product is already exist in order item ,you should update order item'},status=status.HTTP_400_BAD_REQUEST)

       

    except Exception as ex :
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)


# ***  create shippingadress 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_shippingadress(request):
    try :
        print('user create_ orderitem  is==',request.user)
        data = request.data
        serializer = ShippingAdressSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex :
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)


# 2 getOrderById
# مشكلة لا استطيع وضع اكثر من تصريح
class PermissionShowOrder(BasePermission):
    def has_permission(self, request,view):
        pk = view.kwargs['pk']
        order = Order.objects.get(id=pk )
        user  = request.user
        if user.id == order.user.id or request.user.is_superuser :
            return True
        else:
            return False


@api_view(['GET'])
@permission_classes([IsAuthenticated,PermissionShowOrder])
def get_order(request,pk):
    try :
        print('user get_order  is==',request.user)
        order = Order.objects.get(id =pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Order.DoesNotExist :
        return Response({'error':'order not found'},status=status.HTTP_400_BAD_REQUEST)
    except Exception as ex :
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)


# 3 updateOrderToPaid
class PermissionUpdateOrderToPaid(BasePermission):
    def has_permission(self, request,view):
        pk = view.kwargs['pk']
        order = Order.objects.get(id=pk )
        user  = request.user
        if user.id == order.user.id  :
            return True
        else:
            return False
@api_view(['PUT'])
@permission_classes([IsAuthenticated,PermissionUpdateOrderToPaid])
def update_order_to_paid(request,pk):
    try :
        print('user update_order_to_paid  is==',request.user)
        data = request.data
        order = Order.objects.get(id =pk)
        print('data==',data)
        # مشكلة دخال الوقت ايضا 
        date = datetime.now()
        current_date = date.strftime('%Y''-''%m''-''%d')
        if data['is_paid'] != True  or  data['paid_at'] is None or data['paid_at'] != current_date:
            return Response({'error':'you should enter value for is paid is true and paid at current datetime'},status=status.HTTP_400_BAD_REQUEST)

        serializer = OrderSerializer(data = data,instance = order,partial = True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Order.DoesNotExist :
        return Response({'error':'order not found'},status=status.HTTP_400_BAD_REQUEST)
    except Exception as ex :
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)
    
 # 4 getMyOrders
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_myorders(request):
    try :
        print('user get_myorders  is==',request.user)
        user = request.user
        orders = Order.objects.filter(user = user).all()
        if orders :
            serializer = OrderSerializer(orders,many = True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'message':f'user {user.username} have not orders yet'},status=status.HTTP_204_NO_CONTENT)
    except Exception as ex :
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)

 # 5 getAllOrders
@api_view(['GET'])
@permission_classes([IsAuthenticated,IsAdminUser])
def all_orders(request):
    try :
        print('user all_orders ====',request.user)
        orders = Order.objects.all()
        serializer = OrderSerializer(orders,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as ex :
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)

 # 6 updateOrderToDelivered
@api_view(['PUT'])
@permission_classes([IsAuthenticated,IsAdminUser])
def update_order_to_delivered(request,pk):
    try :
        print('user update_order_to_delivered  is==',request.user)
        data = request.data
        order = Order.objects.get(id =pk)
        print('data==',data)
        # مشكلة دخال الوقت ايضا 
        date = datetime.now()
        current_date = date.strftime('%Y''-''%m''-''%d')
        if data['is_delivered'] != True or  data['delivered_at'] is None or data['delivered_at'] != current_date:
            return Response({'error':'you should enter value for is delivered is true and delivered at current datetime'},status=status.HTTP_400_BAD_REQUEST)

        serializer = OrderSerializer(data = data,instance = order,partial = True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Order.DoesNotExist :
        return Response({'error':'order not found'},status=status.HTTP_400_BAD_REQUEST)
    except Exception as ex :
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)
    




  