from rest_framework import serializers
from .models import Product,Review,ImageProduct

# 1
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__' 

# 2
class ImageProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProduct
        fields = '__all__' 

# 3
class ProductSerializer(serializers.ModelSerializer):
    
    userr = serializers.SerializerMethodField()
    def get_userr(seelf,obj):
        return obj.user.username
    
    product_review  = serializers.SerializerMethodField()
    def get_product_review(seelf,obj):
        reviews = obj.review_product.all()
        serializer = ReviewSerializer(reviews,many=True)
        return serializer.data
    
    multi_images  = serializers.SerializerMethodField()
    def get_multi_images(seelf,obj):
        imageproduct = obj.imageproduct_product.all()
        serializer = ImageProductSerializer(imageproduct,many=True)
        return serializer.data
    class Meta:
        model = Product
        fields = '__all__' 

# 4
class Get_One_ProductSerializer(serializers.ModelSerializer):
     
    number_of_review = serializers.SerializerMethodField()
    def get_number_of_review(seelf,obj):
        return obj.review_product.all().count()
    
    sum_rating = serializers.SerializerMethodField()
    def get_sum_rating(seelf,obj):
        reviews = obj.review_product.all()
        list_rating = []
        for review in  reviews:
            list_rating.append(review.rating)
        sum_rating = sum(list_rating)
        return sum_rating    
 
     
    average_rating = serializers.SerializerMethodField()
    def get_average_rating(seelf,obj):
        reviews = obj.review_product.all()
        number_of_review = obj.review_product.all().count()
        if number_of_review != 0 :
            list_rating = []
            for review in  reviews:
                list_rating.append(review.rating)
            sum_rating = sum(list_rating)
            average = sum_rating / number_of_review
            return "sum_rating / number_of_review = ",average
        else :
            return 0
    
            
     
    product_review  = serializers.SerializerMethodField()
    def get_product_review(seelf,obj):
        reviews = obj.review_product.all()
        serializer = ReviewSerializer(reviews,many=True)
        return serializer.data
     
    multi_images  = serializers.SerializerMethodField()
    def get_multi_images(seelf,obj):
        imageproduct = obj.imageproduct_product.all()
        serializer = ImageProductSerializer(imageproduct,many=True)
        return serializer.data
    
    userr = serializers.SerializerMethodField()
    def get_userr(seelf,obj):
        return obj.user.username
    
   
    class Meta:
        model = Product
        fields = '__all__' 