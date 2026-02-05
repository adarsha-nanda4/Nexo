from django.contrib import admin
from django.urls import path,include

from . import productviews as pu
from . import sellerviews as su
from . import adminviews as au
from . import loginviews as lu
from . import views as vu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',vu.dashboard,name='dashboard'),
    path('offline/',vu.offline,name='offline'),
    path('login/',lu.seller_login,name='login'),
    path('logout/',lu.seller_logout,name='logout'),

    path('product_filter/<str:cat>/',pu.p_filter,name='product_filter'),
    path('product_search/',pu.p_search,name='product_search'),

    path('product_detail/<int:pid>/',pu.p_detail,name='product_detail'),

    path('seller/registration/',lu.registration,name='registration'),
    path('seller/profile/',su.profile,name='seller_profile'),
    path('seller/add_edit_product/',su.add_edit_product,name='add_edit_product'),
    path("seller/add_edit_product/<int:product_id>/", su.add_edit_product, name="add_edit_product"),
    path("seller/delete_product/<int:pk>/", su.delete_product, name="delete_product"),
    
]
