from django.urls import path
from . import views
app_name = 'authen'
urlpatterns = [
    path('register_user/',views.register_user,name='register_user'),
    path('users/',views.users,name='users'),
    path('get_profile/',views.get_profile,name='get_profile'),
    path('update_user/<int:pk>/',views.update_user,name='update_user'),
    path('get_user/<int:pk>/',views.get_user,name='get_user'),
    path('delete_user/<int:pk>/',views.delete_user,name='delete_user'),
    path('update_profile/<int:pk>/',views.update_profile,name='update_profile'),

   

]
