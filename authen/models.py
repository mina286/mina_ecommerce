from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    FAM_EML = [
        ('1','female'),
        ('2','male'),
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile_user')
    gender = models.CharField(max_length=30,choices=FAM_EML,default='male')
    age = models.IntegerField(default=6,null=True)
    def __str__(self) :
        return  f"{self.gender}"
    
    class Meta:
        db_table = 'Profile'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'