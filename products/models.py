from django.db import models
from datetime import datetime
from django.urls import reverse


class Products(models.Model):
    title = models.CharField(max_length=300)
    photo = models.ImageField(null=True, blank=True)
    photo2 = models.ImageField(null=True, blank=True)
    photo3 = models.ImageField(null=True, blank=True)
    photo4 = models.ImageField(null=True, blank=True)
    description = models.TextField()
    slug = models.SlugField(max_length=300, unique=True)
    added = models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products', kwargs={'slug':self.slug})

    class Meta:
        verbose_name_plural = 'Products'
