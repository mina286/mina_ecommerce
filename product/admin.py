from django.contrib import admin
from .models import Product,Review,ImageProduct
# Register your models here.
#1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','count_stock']
    list_display_links = ['id','user','name','count_stock']

admin.site.register(Product,ProductAdmin)

# 2
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id','rating','user','product']
    list_display_links = ['id','rating','user','product']

admin.site.register(Review,ReviewAdmin)

# 3
class ImageProductAdmin(admin.ModelAdmin):
    list_display = ['id','product','image']
    list_display_links = ['id','product','image']

admin.site.register(ImageProduct,ImageProductAdmin)
