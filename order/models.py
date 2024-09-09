from django.db import models
from django.contrib.auth.models import User
from product.models import Product,Review
from django.utils import timezone
# Create your models here.
class Order(models.Model):
    PAY_CHIOCES =[
        ('1','visa'),
        ('2','fawry'),
        ('3','cash'),

    ]
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='order_user')
    payment_method = models.CharField(max_length=100,default='visa',choices=PAY_CHIOCES)
    is_paid = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    paid_at = models.DateTimeField(null=True,blank=True)
    delivered_at = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    price = models.FloatField(default=0)
    shipping_price = models.FloatField(default=0)
    total_price = models.FloatField(default=0)
    def __str__(self):
        return f"{self.id}"
    class Meta:
        db_table = 'Order'
        verbose_name ='order'
        verbose_name_plural ='orders'


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True,related_name='orderitem_product')
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name='orderitem_order')
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)

    def __str__(self) :
        return  f"{self.product}"
    class Meta:
        db_table = 'OrderItem'
        verbose_name = 'orderitem'
        verbose_name_plural = 'orderitems'

class ShippingAdress(models.Model):
    order = models.OneToOneField(Order,on_delete=models.CASCADE,related_name='shippingsdress_order')
    country = models.CharField(max_length=100)
    city =  models.CharField(max_length=100)
    postal_code =  models.IntegerField()

    def __str__(self) :
        return  f"{self.order}"
    class Meta:
        db_table = 'ShippingAdress'
        verbose_name = 'shippingadress'
        verbose_name_plural = 'shippingadress'