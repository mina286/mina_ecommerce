from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .serializers import UserSerializer,ProfileSerializers
from .models import Profile
# Create your views here.


# 1 registerUser
@api_view(['POST'])
def register_user(request):
    try :
        print('user register_user is =',request.user)
        data = request.data
        
        serializer = UserSerializer(data =data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)



# 2 login  use it :  path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),



# غير مفهوم استخدام ابي البروفايل ام ابي اليوزر 
# 3 updateUserProfile
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request,pk):
    try :
        user  = User.objects.get(id =pk)
        data = request.data
        print('user list is =',request.user)
        print('data list is =',data)
    
        profile = Profile.objects.get(user = user)
        serializer = ProfileSerializers(data = data,instance = profile,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
    
    except Profile.DoesNotExist :
        return Response({'error':f'Profile not found'},status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)
  

# 4 getUserProfile
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    try :
        print('user getUserProfile is =',request.user)
        user  =request.user
        profile = Profile.objects.get(user = user)
        serializer = ProfileSerializers(profile)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)
    
# 5 getUsers
@api_view(['GET'])
@permission_classes([IsAuthenticated,IsAdminUser])
def users(request):
    try :
        print('users list is =',request.user)
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)
    
# 6 deleteUser
@api_view(['DELETE'])
@permission_classes([IsAuthenticated,IsAdminUser])
def delete_user(request,pk):
    try :
        print('user delte is =',request.user)
        user = User.objects.get(id = pk)
        user.delete()
        return Response({'message':'user is deleted successful'},status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist :
        return Response({'error':f'user not found'},status=status.HTTP_404_NOT_FOUND)
    
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)
    
# 7 getUserById
@api_view(['GET'])
@permission_classes([IsAuthenticated,IsAdminUser])
def get_user(request,pk):
    try :
        print('get user  is =',request.user)
        user = User.objects.get(id = pk)
        serializer = UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    except User.DoesNotExist :
        return Response({'error':f'user not found'},status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)

# 8 updateUser
@api_view(['PUT'])
@permission_classes([IsAuthenticated,IsAdminUser])
def update_user(request,pk):
    try :
        print('user updateUser is =',request.user)
        data = request.data
        user = User.objects.get(id = pk)
        serializer = UserSerializer(data =data,instance = user,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
    except User.DoesNotExist :
        return Response({'error':f'user not found'},status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)



