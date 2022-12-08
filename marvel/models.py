from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import CustomUser
from django.urls import reverse
# Create your models here.


class Marvel(models.Model):
    character =models.CharField(max_length=255)
    name = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    description =models.TextField(default='description')
    image=models.TextField(default='image')

    def __str__(self):
        return self.character

    def get_absolute_url(self):
        return reverse('marvel_list')