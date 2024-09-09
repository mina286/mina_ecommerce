from django.urls import path
from . import views
app_name = 'order'
urlpatterns = [
    path('all_orders/',views.all_orders,name='all_orders'),
    path('create_order/',views.create_order,name='create_order'),
    path('create_orderitem/',views.create_orderitem,name='create_orderitem'),
    path('create_shippingadress/',views.create_shippingadress,name='create_shippingadress'),
    path('get_myorders/',views.get_myorders,name='get_myorders'),
    path('get_order/<int:pk>/',views.get_order,name='get_order'),
    path('update_order_to_paid/<int:pk>/',views.update_order_to_paid,name='update_order_to_paid'),
    path('update_order_to_delivered/<int:pk>/',views.update_order_to_delivered,name='update_order_to_delivered'),




]
