from django.urls import path, include

from .views import *

#   from . import view as v
#
#   urlpatterns = [
#       path('login/', v.company_login, name='c_login'),
#       path('Registration/', v.company_register, name='c_register')
#   ]

urlpatterns = [
    path('', Company_login, name='c_login'),
    path('registration/', Company_register, name='c_register'),
    path('Dashboard/',Dashboard,name='Dashboard'),
    path('OTP_check/',OTP_check,name='OTP_check'),
    path('New_pass/',New_pass,name='New_pass'),
    path('Comp_forgetpass/', Comp_forgetpass, name='Comp_forgetpass'),
]