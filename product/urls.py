from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPageProducts.as_view(), name = "home_page"),
    path('create_product', AddProduct.as_view(), name = "add_product"),
    path('view_product/<int:pk>/', ViewProduct.as_view(), name = "view_product"),
]