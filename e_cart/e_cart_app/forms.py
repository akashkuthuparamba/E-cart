from django.forms import ModelForm
from . models import Item,UserDetails
from django.contrib.auth.models import User

class ItemForm(ModelForm):
    class Meta:
        model=Item
        fields='__all__'

# class LoginForm(ModelForm):
#     class Meta:
#         model=User
#         fields=("username","password")


class RegisterForm(ModelForm):
    class Meta:
        model=UserDetails
        fields=("username","password","first_name","last_name","address","email","phone_no")        

class DetailEditForm(ModelForm):
    class Meta:
        model=UserDetails
        fields=("first_name","last_name","address","email","phone_no")              