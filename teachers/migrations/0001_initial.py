# Generated by Django 5.1.5 on 2025-02-14 08:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('qualification', models.CharField(max_length=100)),
                ('join_date', models.DateField()),
                ('employment_type', models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('contract', 'Contract')], max_length=20)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='teachers/')),
                ('is_active', models.BooleanField(default=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.department')),
                ('subjects', models.ManyToManyField(related_name='teachers', to='subjects.subject')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
