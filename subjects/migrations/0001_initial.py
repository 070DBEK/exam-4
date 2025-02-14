# Generated by Django 5.1.5 on 2025-02-14 08:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('credit_hours', models.PositiveIntegerField()),
                ('grade_level', models.CharField(choices=[('9', '9th Grade'), ('10', '10th Grade'), ('11', '11th Grade')], help_text='Select the grade level for this subject.', max_length=2)),
                ('prerequisites', models.CharField(blank=True, choices=[('math', 'Mathematics'), ('phy', 'Physics'), ('chem', 'Chemistry'), ('bio', 'Biology'), ('eng', 'English'), ('hist', 'History'), ('geo', 'Geography'), ('cs', 'Computer Science')], help_text='Select a prerequisite subject.', max_length=50, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='departments.department')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
