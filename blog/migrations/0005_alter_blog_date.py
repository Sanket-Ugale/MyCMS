# Generated by Django 4.1.7 on 2023-03-11 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_blog_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="date",
            field=models.DateField(verbose_name="Date"),
        ),
    ]
