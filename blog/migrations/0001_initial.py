# Generated by Django 4.1.7 on 2023-03-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="blog",
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
                ("Title", models.CharField(max_length=30)),
                ("description", models.CharField(max_length=40)),
                ("url", models.CharField(max_length=100)),
                ("banner", models.ImageField(upload_to="images/")),
                ("content", models.TextField()),
            ],
        ),
    ]
