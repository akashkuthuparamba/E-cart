from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20,default=None)
    def __str__(self):
        return self.name

class Item(models.Model):
    item_name=models.CharField(max_length=100,default=None)
    item_price=models.IntegerField(default=None)
    item_img=models.ImageField(upload_to='media/',default=None)
    quantitie=models.CharField(max_length=30, default=None)
    brand_name=models.CharField(max_length=100, default=None)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='item',default=None)
    def __str__(self):
        return self.item_name

class UserDetails(AbstractUser):
    address=models.TextField(default=None ,null=True)
    phone_no=models.IntegerField(default=None, null=True)
