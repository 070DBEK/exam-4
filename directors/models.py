from django.db import models

class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
    birth = models.DateField()
    picture = models.ImageField(upload_to='directors/', blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
