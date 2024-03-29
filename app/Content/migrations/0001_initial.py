# Generated by Django 4.1.13 on 2024-02-01 00:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('course_name', models.CharField(max_length=500)),
                ('module', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('video_url', models.FileField(blank=True, upload_to='assets/coursesVideos/content/')),
            ],
        ),
    ]
