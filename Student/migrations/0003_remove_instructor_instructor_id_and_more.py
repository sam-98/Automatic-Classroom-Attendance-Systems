# Generated by Django 4.1.2 on 2022-11-14 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Student", "0002_alter_course_table_alter_dailyattendance_table_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="instructor", name="instructor_id",),
        migrations.AlterField(
            model_name="instructor",
            name="mail",
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
