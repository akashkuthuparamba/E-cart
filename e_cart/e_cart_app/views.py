from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from.forms import ItemForm,RegisterForm,DetailEditForm
from.models import Item,UserDetails,Category,PurchaseDetails,CartDetails,Review
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
import datetime
# Create your views here.


def home_view(request):
    form=ItemForm()
    if request.method=="POST":
        form=ItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('e_cart_app:list')
    return render(request,'home.html',{'form':form})

def list(request):
    data=Item.objects.all()
    cate=Category.objects.all()
    if request.method=='POST':

        search=request.POST['search']
        print(search)
        data=Item.objects.filter(item_name=search)
        return render(request,'list.html',{"data":data})   

        
    return render(request,'list.html',{"data":data,"cate":cate})   

def details(request,id):
    data=Item.objects.get(id=id)
    print(type(data))
    if request.method=="POST":
        q=data.item_name
        print(type(q))
        item=data
        message=request.POST['review']
        date=datetime.datetime.now().date()
        time=datetime.datetime.now().time()
        user=request.user.username
        details=Review.objects.create(message=message,date=date,time=time,name=user,item=item)
        details.save()



    return render(request,'details.html',{"data":data})    



def login_view(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        myuser=authenticate(username=username,password=password)
        print(myuser)
        if myuser is not None:
            print("logged in")
            login(request,myuser)
            return redirect('/')
    # form=LoginForm()            
    return render(request,'login.html')


def register_view(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            email=request.POST['email']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            address=request.POST['address']
            phone_no=request.POST['phone_no']
            myuser=UserDetails.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name,address=address,phone_no=phone_no)
            print(myuser)
            myuser.save()
            return redirect('e_cart_app:login')
    form=RegisterForm()      
    return render(request,'register.html',{"form":form})



def choice(request):
    return render(request,"choice.html")


def logout_view(request):
    logout(request)
    return redirect('e_cart_app:list')



def buy_view(request,id):
    data=request.user
    details=Item.objects.get(id=id)
    
    return render(request,'buy.html',{"data":data,"details":details})


def edit_view(request,id):
    data=request.user
    form=DetailEditForm()
    if request.method=="POST":
        form=request.POST
        data.first_name=request.POST['first_name']
        data.last_name=request.POST['last_name']
        data.address=request.POST['address']
        data.email=request.POST['email']
        data.phone_no=request.POST['phone_no']
        data.save()
        print(id)
        # return redirect('buy' , id=id)
        return redirect("e_cart_app:buy", id)

        # return HttpResponse("details changed go back")
    return render(request,'edit.html',{"form":form})


def success_view(request,pk):
    user=request.user
    details=Item.objects.get(pk=pk)
    name=details.item_name
    price=details.item_price
    quantitie=details.quantitie
    item=user
    date=datetime.date.today()
    purchase=PurchaseDetails.objects.create(name=name,price=price,quantitie=quantitie,item=user,date=date)
    purchase.save()

    
    return render(request,'success.html',{"user":user})


# def search_view(request):
#     if request.method=="GET":
#         print("get")
#         print(request)

#         data=request.GET.get('search')
#         print(data)
#     return render(request,'list.html')   

def cate_view(request,name,pk):
    print(pk)
    data=Category.objects.filter(pk=pk)
    # query set aan kittunnnath athil group of object nd
    print(data)
    return render(request,'cate.html',{"data":data})



def purchace_view(request):
    user=request.user
    data=UserDetails.objects.get(username=user)
    print(data)

    return render(request,"purchace.html",{"data":data})


def user_view(request):
    user=request.user
    data=UserDetails.objects.get(username=user)
    return render(request,'user.html',{"user":user,"data":data})



def cart_view(request,pk):
         
    user=request.user
    details=Item.objects.get(pk=pk)
    name=details.item_name
    price=details.item_price
    quantitie=details.quantitie
    user=user
    date=datetime.date.today()
    purchase=CartDetails.objects.create(name=name,price=price,quantitie=quantitie,item=user,date=date)
    purchase.save()
    data=UserDetails.objects.get(username=user)
    return redirect('/cart_display/')



def cart_display(request):
    user=request.user.pk

    data=UserDetails.objects.get(pk=user)
    return render(request,'cart.html',{"data":data})


def cart_delete(request,pk):
    CartDetails.objects.get(pk=pk).delete()

    return redirect('/cart_display/')


def filter_view(request,pk,id):
    data=Category.objects.get(pk=pk)

    return render(request,'filter.html',{"data":data,"id":id}) 