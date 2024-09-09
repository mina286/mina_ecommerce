from django.urls import path
from . import views
app_name = 'product'
urlpatterns = [
    path('products/',views.products,name='products'),
    path('greate_product/',views.greate_product,name='greate_product'),
    path('greate_review/',views.greate_review,name='greate_review'),
    path('products/<int:pk>/',views.get_product,name='get_product'),
    path('update_product/<int:pk>/',views.update_product,name='update_product'),
    path('products_delete/<int:pk>/',views.delete_product,name='delete_product'),
    #
    path('greate_image_product/',views.greate_image_product,name='greate_image_product'),

]
