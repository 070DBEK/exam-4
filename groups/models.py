from django.db import models
from django.urls import reverse
from departments.base_model import BaseModel
from teachers.models import Teacher
from subjects.models import Subject
from django.utils.text import slugify
from django.urls import reverse
import random


class Group(BaseModel):
    GRADE_LEVEL_CHOICES = [
        (9, "Grade 9"),
        (10, "Grade 10"),
        (11, "Grade 11"),
    ]

    SCHEDULE_CHOICES = [
        ("morning", "Morning Session"),
        ("afternoon", "Afternoon Session"),
        ("evening", "Evening Session"),
    ]

    name = models.CharField(max_length=255)
    grade_level = models.IntegerField(choices=GRADE_LEVEL_CHOICES)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    schedule = models.CharField(max_length=20, choices=SCHEDULE_CHOICES)
    academic_year = models.CharField(max_length=20)
    max_students = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    subjects = models.ManyToManyField(Subject, related_name='groups')
    students = models.ManyToManyField("students.Student", related_name="groups", blank=True)

    def get_absolute_url(self):
        return reverse("groups:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) + "-" + str(random.randint(1,100))
        super().save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('groups:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])