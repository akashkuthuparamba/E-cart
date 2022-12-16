from django.urls import path
from.views import home_view,list,details,login_view,register_view,choice,logout_view,buy_view,edit_view,success_view,cate_view,purchace_view,user_view,cart_view,cart_display,cart_delete,filter_view
from django.conf import settings
from django.conf.urls.static import static

app_name="e_cart_app"

urlpatterns=[
    path('home/',home_view,name="home"),
    path('',list,name='list'),
    path('<int:id>/',details,name='details'),
    path('login/',login_view,name='login'),
    path('register/',register_view,name='register'),
    path('choice/',choice,name='choice'),
    path('logout/',logout_view,name='logout'),
    path('<int:id>/buy/',buy_view,name='buy'),
    path('<int:id>/buy/edit/',edit_view,name='edit'),
    path('<int:pk>/success/',success_view,name="success"),
    path('<str:name>/<int:pk>',cate_view,name='frts'),
    path('purchacedetails/',purchace_view,name='purchacedetails'),
    path('user/',user_view,name='user'),
    path('<int:pk>/cart/',cart_view,name="cart"),
    path('cart_display/',cart_display,name="cart_display"),
    path('<int:pk>/cart_delete',cart_delete,name="delete"),
    path('<int:pk>/<int:id>/fillter',filter_view,name="filter"),





  



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)