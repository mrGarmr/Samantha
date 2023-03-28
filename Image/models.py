from django.db import models
from django.conf import settings


class Picture(models.Model):
    name = models.ImageField(upload_to='images', blank=True)

    # owner = models.TextField(max_length=100)
    uploaded_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    prediction = models.TextField(max_length=100)

    def __str__(self):
        return self.prediction

