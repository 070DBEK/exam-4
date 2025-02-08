from django.db import models
from departments.models import Department


class Subject(models.Model):
    SUBJECT_CHOICES = [
        ('math', 'Mathematics'),
        ('phy', 'Physics'),
        ('chem', 'Chemistry'),
        ('bio', 'Biology'),
        ('eng', 'English'),
        ('hist', 'History'),
        ('geo', 'Geography'),
        ('cs', 'Computer Science'),
    ]

    GRADE_CHOICES = [
        ('9', '9th Grade'),
        ('10', '10th Grade'),
        ('11', '11th Grade'),
    ]

    name = models.CharField(max_length=100, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="subjects")
    description = models.TextField()
    credit_hours = models.PositiveIntegerField()

    grade_level = models.CharField(
        max_length=2,
        choices=GRADE_CHOICES,
        help_text="Select the grade level for this subject."
    )

    prerequisites = models.CharField(
        max_length=50,
        choices=SUBJECT_CHOICES,
        blank=True,
        null=True,
        help_text="Select a prerequisite subject."
    )

    def __str__(self):
        return self.name
