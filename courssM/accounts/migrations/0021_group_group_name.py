# Generated by Django 4.2.4 on 2023-10-19 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0020_group_student_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="group",
            name="group_name",
            field=models.CharField(max_length=25, null=True),
        ),
    ]