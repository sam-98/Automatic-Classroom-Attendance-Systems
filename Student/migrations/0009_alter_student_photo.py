# Generated by Django 4.1.2 on 2022-11-17 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Student", "0008_alter_takes_attendace_percentage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="photo",
            field=models.ImageField(default="", null=True, upload_to="images/"),
        ),
    ]
