# Generated by Django 4.2.4 on 2023-10-17 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0015_alter_user_managers"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="session_hours",
            field=models.FloatField(default=0),
        ),
    ]
