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


class PurchaseDetails(models.Model):
    name=models.CharField(max_length=30,default=None)
    price=models.CharField(max_length=10,default=None)
    quantitie=models.CharField(max_length=30,default=None)
    date=models.DateField(default=None)
    item=models.ForeignKey(UserDetails,on_delete=models.CASCADE,related_name='details',default=None) 


class CartDetails(models.Model):
    name=models.CharField(max_length=30,default=None)
    price=models.CharField(max_length=10,default=None)
    quantitie=models.CharField(max_length=30,default=None)
    date=models.DateField(default=None)
    item=models.ForeignKey(UserDetails,on_delete=models.CASCADE,related_name='cart',default=None) 


class Review(models.Model):
    name=models.CharField(max_length=20, default=None)
    message=models.TextField(default=None)
    date=models.DateField(default=None)
    time=models.TimeField(default=None)
    item=models.ForeignKey(Item,on_delete=models.CASCADE,related_name='msg',default=None)

