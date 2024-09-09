from django.contrib import admin
from .models import Order,OrderItem,ShippingAdress
# Register your models here.
# 1
class OrderAdmin(admin.ModelAdmin):
    list_display =['id','user','payment_method']
    list_display_links = ['id','user','payment_method']

admin.site.register(Order,OrderAdmin)

# 2
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id','quantity','product','order']
    list_display_links = ['id','quantity','product','order']

admin.site.register(OrderItem,OrderItemAdmin)

# 3
class ShippingAdressAdmin(admin.ModelAdmin):
    list_display = ['id','order','country','city']
    list_display_links = ['id','order','country','city']

admin.site.register(ShippingAdress,ShippingAdressAdmin)