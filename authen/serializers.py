from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
# 1

class ProfileSerializers(serializers.ModelSerializer):
    # مشكلة عدم ظهور اليوزر داخل البروفايل والعكس صحيح وهو يجب ساتخدامة داخل واحده منهم فقط
    #image = serializers.ImageField(max_length=None, allow_empty_file=False)
    """ 
    user = serializers.SerializerMethodField()
    def get_user(self,obj):
        user = obj.user
        serializer = UserSerializer(user)
        return serializer.data
    """
    class Meta:
        model = Profile
        fields= "__all__"

 
# 2
class UserSerializer(serializers.ModelSerializer):
     
    profile = serializers.SerializerMethodField()
    def get_profile(self,obj):
        if hasattr(obj,'profile_user') :
            prof = obj.profile_user
            serializer = ProfileSerializers(prof)
            return serializer.data
        else :
            return {}
    
    class Meta:
        model = User
        fields= "__all__"

