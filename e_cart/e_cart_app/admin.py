from django.contrib import admin
from . models import Item,UserDetails,Category,PurchaseDetails,CartDetails,Review

# Register your models here.

admin.site.register(Item)
admin.site.register(UserDetails)
admin.site.register(Category)
admin.site.register(PurchaseDetails)
admin.site.register(CartDetails)
admin.site.register(Review)