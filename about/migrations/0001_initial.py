# Generated by Django 3.0 on 2020-04-17 04:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.TextField()),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='about_images/')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='about_images/')),
            ],
            options={
                'verbose_name_plural': 'About',
            },
        ),
        migrations.CreateModel(
            name='Proceedue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Proceedue',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('work', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Team Members',
            },
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField()),
                ('added', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'Testimonials',
            },
        ),
    ]
