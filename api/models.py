from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass


class Honeypot(models.Model):
    name = models.CharField(max_length=50)
    container_id = models.CharField(max_length=100)
    container_ip = models.CharField(max_length=15)
    container_conf = models.CharField(max_length=10000)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='containers')

    def __str__(self):
        return f'{self.name} - {self.container_id}'
