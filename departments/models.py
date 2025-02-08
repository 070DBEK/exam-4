from django.db import models
from directors.models import Director


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    head = models.OneToOneField(Director, on_delete=models.SET_NULL, null=True, blank=True, related_name='department')
    description = models.TextField()
    location = models.CharField(max_length=255)
    contact_email = models.EmailField(unique=True)
    contact_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name