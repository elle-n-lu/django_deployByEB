# Generated by Django 4.2.4 on 2023-10-19 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0021_group_group_name"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Group",
            new_name="Student_Group",
        ),
    ]
