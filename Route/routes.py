from django.contrib import admin
from django.urls import path,include

from . import productviews as pu
from . import sellerviews as su
from . import adminviews as au
from . import loginviews as lu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',pu.home,name='dashboard'),
    path('login/',lu.seller_login,name='login'),


    path('seller/registration/',su.registration,name='registration'),
    
]
