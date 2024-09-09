from django.shortcuts import render
from .serializers import ProductSerializer,Get_One_ProductSerializer,ReviewSerializer,ImageProductSerializer
from .models import Product,Review,ImageProduct
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser,BasePermission
import json

############ products ##################
# 1  getProducts
@api_view(['GET'])
def products(request):
    try :
        products = Product.objects.all()
        serializer = ProductSerializer(products,many = True)
        return Response(serializer.data,status= status.HTTP_200_OK)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status= status.HTTP_400_BAD_REQUEST)

# 2 getProduct
@api_view(['GET'])
def get_product(request,pk):
    try :
        products = Product.objects.get(id = pk)
        serializer = Get_One_ProductSerializer(products)
        return Response(serializer.data,status= status.HTTP_200_OK)
    except Product.DoesNotExist :
        return Response({'error':f'product not found'},status= status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status= status.HTTP_400_BAD_REQUEST)
    
# 3 deleteProduct
@api_view(['DELETE'])
@permission_classes([IsAuthenticated,IsAdminUser])
def delete_product(request,pk):
    try :
        print('user is delte product====',request.user)
        product = Product.objects.get(id = pk)
        product.delete()
        return Response({'message':'product is deleted'},status= status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist :
        return Response({'error':f'product not found'},status= status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status= status.HTTP_400_BAD_REQUEST)
    
# 4 createProduct
@api_view(['POST'])
@permission_classes([IsAuthenticated,IsAdminUser])
def greate_product(request):
    try :
        print('user is create product====',request.user)
        data = request.data
        serializer = ProductSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status= status.HTTP_400_BAD_REQUEST)
    
# 5 updateProduct 
@api_view(['PUT'])
@permission_classes([IsAuthenticated,IsAdminUser])
def update_product(request,pk):
    try :
        product = Product.objects.get(id = pk)
        data = json.loads(request.body)
        serializer = ProductSerializer(data = data,instance = product,partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status= status.HTTP_400_BAD_REQUEST)

# 6 uploadImage * note *-- upload image from form-data in postman
@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def greate_image_product(request):
    try :
        print('user is greate_imageproduct ====',request.user)
        data = request.data
        print('dataaaa=',data)
        serializer = ImageProductSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status= status.HTTP_400_BAD_REQUEST)
    


# 7 createProductReview
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def greate_review(request):
    try :
        print('user is create review====',request.user)
        data = request.data
        serializer = ReviewSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status= status.HTTP_400_BAD_REQUEST)
    
