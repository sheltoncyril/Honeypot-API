from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now
class User(AbstractUser):
    id= models.UUIDField(primary_key= True, editable=False, default=uuid.uuid4)
    
class HoneypotTemplate(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    config = models.CharField(max_length=10000)

    def __str__(self):
        return f"{self.name} Template"

class Honeypot(models.Model):
    id = models.UUIDField(primary_key= True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    template = models.ForeignKey(HoneypotTemplate, on_delete=models.CASCADE, related_name='template')
    container_id = models.CharField(max_length=100, blank=True, null=True)
    container_ip = models.GenericIPAddressField(blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='honeypots', default="None")

    def __str__(self):
        return f'{self.name} - {self.container_id}'

class Trigger(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    Honeypot = models.ForeignKey(Honeypot, on_delete=models.CASCADE,related_name='triggers')
    source_ip = models.GenericIPAddressField()
    port = models.PositiveIntegerField(default=80, validators=[MinValueValidator(0),MaxValueValidator(65535)])
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    log_time = models.DateTimeField(default=now, editable=False)
    full_log = models.TextField(blank=True)
    def __str__(self):
        return f'{self.Honeypot} {self.log_time}'