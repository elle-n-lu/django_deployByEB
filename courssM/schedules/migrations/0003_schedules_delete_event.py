# Generated by Django 4.2.4 on 2023-10-12 23:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("schedules", "0002_event_creator"),
    ]

    operations = [
        migrations.CreateModel(
            name="Schedules",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("description", models.TextField()),
                (
                    "sche_creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schedule_creator",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Event",
        ),
    ]
