# Generated by Django 4.2.4 on 2023-10-29 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0023_courseallocation_created_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="courseallocation",
            name="course_length",
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
