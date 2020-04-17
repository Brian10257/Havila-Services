from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView
from .models import Products

class ProductsList(generic.ListView):
    queryset = Products.objects.order_by('-added')
    model = Products
    template_name = 'pages/products.html'
    paginate_by = 9

def product(request, slug):
    detail = get_object_or_404(Products, slug=slug)
    return render(request, 'pages/products_detail.html', {'detail':detail})