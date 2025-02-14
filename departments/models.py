from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import random
from directors.models import Director
from .base_model import BaseModel


class Department(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    head = models.OneToOneField(Director, on_delete=models.SET_NULL, null=True, blank=True, related_name='department')
    description = models.TextField()
    location = models.CharField(max_length=255)
    contact_email = models.EmailField(unique=True)
    contact_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) + "-" + str(random.randint(1,100))
        super().save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('departments:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])
