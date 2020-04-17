from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView
from . models import Services


class ServicesList(generic.ListView):
    queryset = Services.objects.order_by('-added')
    model = Services
    paginate_by =9
    template_name = 'pages/services.html'



def services(request, slug):
    detail = get_object_or_404(Services, slug=slug)
    return render(request, 'pages/services_detail.html', {'detail':detail})