# Generated by Django 4.2.4 on 2023-10-16 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0009_alter_course_session_course_dates"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course_session",
            name="course_dates",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
