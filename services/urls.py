from django.urls import path
from . import views

urlpatterns = [
    path('services', views.ServicesList.as_view(), name = 'services'),
    path('<slug>', views.services, name = 'services'),
]