# Generated by Django 5.1.5 on 2025-02-08 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(choices=[('9', 'Grade 9'), ('10', 'Grade 10'), ('11', 'Grade 11')], max_length=2),
        ),
    ]
