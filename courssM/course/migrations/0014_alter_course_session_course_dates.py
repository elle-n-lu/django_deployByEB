# Generated by Django 4.2.4 on 2023-10-16 05:40

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0013_alter_course_session_course_dates"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course_session",
            name="course_dates",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.JSONField(blank=True, default=dict, null=True),
                blank=True,
                default=[],
                max_length=250,
                size=None,
            ),
        ),
    ]
