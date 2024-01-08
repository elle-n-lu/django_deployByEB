# Generated by Django 4.2.4 on 2023-10-15 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0008_course_session"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course_session",
            name="course_dates",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Monday", "Monday"),
                    ("Tuesday", "Tuesday"),
                    ("Wednesday", "Wednesday"),
                    ("Thursday", "Thursday"),
                    ("Friday", "Friday"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]
