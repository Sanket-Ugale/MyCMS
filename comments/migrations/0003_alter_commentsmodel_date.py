# Generated by Django 4.1.7 on 2023-03-24 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0002_commentsmodel_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commentsmodel",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
