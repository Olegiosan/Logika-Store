from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from product.forms import AddProductForm
from product.models import Product


# Create your views here.
class MainPageProducts(ListView):
    template_name = "product/main_page.html"
    model = Product
    context_object_name = "products"

class AddProduct(CreateView, LoginRequiredMixin):
    template_name = "product/add_product.html"
    model = Product
    form_class = AddProductForm
    success_url = reverse_lazy("home_page")

class ViewProduct(DetailView):
    template_name = "product/view_product.html"
    model = Product
    context_object_name = "product"