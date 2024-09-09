from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator,MinValueValidator,MaxValueValidator
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='product_user')
    name = models.CharField(max_length=100,unique=True,validators=[MinLengthValidator(5)])
    brand = models.CharField(max_length=100,validators=[MinLengthValidator(5)])
    category = models.CharField(max_length=100,validators=[MinLengthValidator(5)])
    price = models.FloatField(validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='product_image/',default='/def/d.png',null=True,blank=True)
    num_review = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(null=True,blank=True)
    count_stock = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return  self.name
    class Meta:
        db_table = 'Product'
        verbose_name = 'product'
        verbose_name_plural = 'products'
        constraints = [
            models.UniqueConstraint(fields=['name'],name='name_unique'),
            models.CheckConstraint(check=models.Q(name__gte=5),name='name_gte_5'),
            models.CheckConstraint(check=models.Q(brand__gte=5),name='brand_gte_5'),
            models.CheckConstraint(check=models.Q(category__gte=5),name='category_gte_5'),
            models.CheckConstraint(check=models.Q(price__gte=0),name='price_gte_0'),
            models.CheckConstraint(check=models.Q(num_review__gte=0),name='num_review_gte_0'),
            models.CheckConstraint(check=models.Q(count_stock__gte=0),name='count_stock_gte_0'),

        ]

class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='review_product')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='review_user')
    text = models.TextField(null=True,blank=True)
    rating = models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0),MaxValueValidator(5)])
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return  f"{self.product}--{self.user}"
    class Meta:
        db_table = 'Review'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        constraints = [
            models.CheckConstraint(check=models.Q(rating__gte=0)&models.Q(rating__lte=5),name='name_gte_0'),

        ]

class ImageProduct(models.Model):
   product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='imageproduct_product')
   image = models.ImageField(upload_to='multi_image_product/',null=True,blank=True)

   def __str__(self):
        return str(self.product)
   
   class Meta:
        db_table = 'ImageProduct'
        verbose_name = 'ImageProduct'
        verbose_name_plural = 'ImageProducts'
       