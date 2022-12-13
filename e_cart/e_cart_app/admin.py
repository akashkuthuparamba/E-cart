from django.contrib import admin
from . models import Item,UserDetails,Category

# Register your models here.

admin.site.register(Item)
admin.site.register(UserDetails)
admin.site.register(Category)