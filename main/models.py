from django.db import models
from django.conf import settings
from django.utils import timezone

class Contact(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    def __str__(self):
        return self.text