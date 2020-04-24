from django.db import models
from datetime import datetime

class About(models.Model):
    history = models.TextField()
    photo1 = models.ImageField(upload_to='about_images/', blank=True, null = True)
    photo2 = models.ImageField(upload_to='about_images/', blank=True, null = True)
    def __str__(self):
        return self.history
    class Meta:
        verbose_name_plural = 'About'

class Proceedue(models.Model):
    title = models.CharField(max_length=30)
    count = models.IntegerField()
    description = models.TextField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Proceedue'

class Team(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=50)
    work = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Team Members'

class Testimonials(models.Model):
    title =models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    added = models.DateTimeField(default = datetime.now, blank = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Testimonials'
