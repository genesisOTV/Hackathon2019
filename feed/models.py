from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from multi_email_field.fields import MultiEmailField
from django.urls import reverse

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    amount = models.IntegerField(default=0)
    members = MultiEmailField(blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    end_date = models.DateTimeField(default=datetime.now, blank=True)

    def get_absolute_url(self):
        return reverse('mainview')