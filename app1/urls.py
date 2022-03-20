from django.urls import path, include

from .views import *

#   from . import view as v
#
#   urlpatterns = [
#       path('login/', v.company_login, name='c_login'),
#       path('Registration/', v.company_register, name='c_register')
#   ]

urlpatterns = [
    path('signin/', Sign_in, name='signin'),
    path('signup/', Sign_up, name='signup'),
    path('', home, name='home'),
    path('Comp_forgetpass/', Comp_forgetpass, name='Comp_forgetpass'),
    path('New_pass/',New_pass,name='New_pass'),
    path('Dashboard/',Dashboard,name='Dashboard'),
    path('OTP_check/',OTP_check,name='OTP_check'),

# ============== web page =================

    path('cart/',Cart,name='cart'),
    path('checkout/',Checkout,name='checkout'),
    path('contacts/',Contacts,name='contacts'),
    path('my_account/',My_account,name='my_account'),
    path('product_details/',Product_details,name='product_details'),
    path('product_list/',Product_list,name='product_list'),
    path('wishlist/',Wishlist,name='wishlist'),
    

    
    
]