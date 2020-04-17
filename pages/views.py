from django.shortcuts import render
from services.models import Services
from products.models import Products
from blogs.models import Blog, Comment

def index(request):
    services = Services.objects.order_by('-added')[:3]
    products = Products.objects.order_by('-added')[:6]
    post = Blog.objects.order_by('-date_published')[:3]
    comment = Comment.objects.all()
    context = {
        'services':services,
        'products':products,
        'post':post,
        'comment':comment
    }
    return render(request, 'pages/index.html', context)