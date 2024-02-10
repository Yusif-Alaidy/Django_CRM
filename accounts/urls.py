from django.urls import path 
from .views      import *

urlpatterns = [
    path('home',     home,     name='home'),
    path('product',  product,  name='product'),
    path('customer', customer, name='customer'),
]
