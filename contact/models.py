from django.db import models
from datetime import datetime


class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300, blank = True)
    phone = models.CharField(max_length=300, blank = True)
    subject = models.CharField(max_length = 300, blank=True)
    message = models.TextField()
    contacted = models.DateTimeField(default = datetime.now, blank = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Recieved Messages'