# Generated by Django 4.1.2 on 2023-01-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foobar", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="log",
            name="level",
            field=models.CharField(
                choices=[
                    ("DBG", "Debug"),
                    ("INF", "Info"),
                    ("WRN", "Warning"),
                    ("ERR", "Error"),
                ],
                max_length=3,
            ),
        ),
    ]