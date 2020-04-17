from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('about/', include('about.urls')),
    path('contact-us/', include('contact.urls')),
    path('our-blogs/', include('blogs.urls')),
    path('our-products/', include('products.urls')),
    path('services/', include('services.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
