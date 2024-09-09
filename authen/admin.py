from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User

# Register your models here.
# 1
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','age','gender']
    list_display_links = ['id','user','age','gender']

admin.site.register(Profile,ProfileAdmin)
# 2
