from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginUserView.as_view(), name = "user_login"),
    path('register/', CreateUser.as_view(), name = "create_user")
]