# Generated by Django 4.2.4 on 2023-10-17 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0018_remove_courseallocation_courses_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="course_session",
            name="delivered",
            field=models.BooleanField(default=False),
        ),
    ]
