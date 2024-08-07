# Generated by Django 5.0.8 on 2024-08-07 05:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SQLToken",
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
                ("userId", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("token", models.CharField(max_length=128)),
            ],
        ),
    ]
