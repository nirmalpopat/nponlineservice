from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from datetime import datetime

class Sells(models.Model):
    agent_name = models.CharField(max_length=10)
    item_name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    comment = models.CharField(max_length=50, blank=True, null=True)
    timing = models.DateTimeField(default=datetime.now)