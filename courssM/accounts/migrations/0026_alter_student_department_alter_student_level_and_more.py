# Generated by Django 4.2.4 on 2023-10-29 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0024_courseallocation_course_length"),
        ("accounts", "0025_alter_student_parent_alter_student_student_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="department",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="course.program",
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="level",
            field=models.CharField(
                blank=True,
                choices=[("Bachloar", "Bachloar Degree"), ("Master", "Master Degree")],
                max_length=25,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="session_hours",
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
