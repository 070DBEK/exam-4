from django.db import models
from departments.models import Department
from subjects.models import Subject


class Teacher(models.Model):
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
    is_active = models.BooleanField(default=True)  # ✅ Yangi maydon qo'shildi

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
