# Generated by Django 4.1.7 on 2023-03-25 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_alter_blog_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="author",
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
    ]
