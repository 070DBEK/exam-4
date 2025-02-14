from django.db import models
from departments.models import Department
from subjects.models import Subject
from departments.base_model import BaseModel
from django.utils.text import slugify
from django.urls import reverse
import random


class Teacher(BaseModel):
    EMPLOYMENT_TYPES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    qualification = models.CharField(max_length=100)
    join_date = models.DateField()
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, related_name="teachers")
    profile_photo = models.ImageField(upload_to='teachers/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.last_name, self.first_name) + "-" + str(random.randint(1,100))
        super().save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('teachers:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])
