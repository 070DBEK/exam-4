from django.db import models
from groups.models import Group
from django.utils.text import slugify
from django.urls import reverse
import random
from departments.base_model import BaseModel


class Student(BaseModel):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    GRADE_CHOICES = [
        ('9', 'Grade 9'),
        ('10', 'Grade 10'),
        ('11', 'Grade 11'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    parent_name = models.CharField(max_length=100)
    parent_phone = models.CharField(max_length=15)
    parent_email = models.EmailField()
    profile_photo = models.ImageField(upload_to='students/photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.last_name, self.first_name) + "-" + str(random.randint(1,100))
        super().save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('students:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])
