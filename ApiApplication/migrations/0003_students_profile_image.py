# Generated by Django 4.1.3 on 2023-01-28 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApplication', '0002_rename_course_duaration_courses_course_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='profile_image',
            field=models.ImageField(default='None.jpg', upload_to='Images'),
        ),
    ]
