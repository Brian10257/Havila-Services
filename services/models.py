from django.db import models
from datetime import datetime
from django.urls import reverse

class Services(models.Model):
    title = models.CharField(max_length=300)
    item_photo = models.ImageField()
    author = models.CharField(max_length=300, blank=True)
    description = models.TextField()
    slug = models.SlugField(max_length=300, unique=True)
    added = models.DateTimeField(default = datetime.now, blank = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Services'