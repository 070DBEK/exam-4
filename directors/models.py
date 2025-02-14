from django.db import models
from departments.base_model import BaseModel
from django.utils.text import slugify
import random
from django.urls import reverse


class Director(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
    birth = models.DateField()
    picture = models.ImageField(upload_to='directors/', blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.last_name, self.first_name) + "-" + str(random.randint(1,100))
        super().save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('directors:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])