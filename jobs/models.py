from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('pending', 'Pending'),
        ('interview', 'Interview Scheduled'),
        ('rejected', 'Rejected'),
        ('offer', 'Offer Received'),
    ]
    title = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    applied_date = models.DateField(auto_now=True)
    notes = models.TextField(blank=True)
