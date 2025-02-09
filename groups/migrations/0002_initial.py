# Generated by Django 5.1.5 on 2025-02-09 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        ('students', '0001_initial'),
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='groups', to='students.student'),
        ),
        migrations.AddField(
            model_name='group',
            name='subjects',
            field=models.ManyToManyField(related_name='groups', to='subjects.subject'),
        ),
    ]
