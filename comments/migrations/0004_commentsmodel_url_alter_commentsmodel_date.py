# Generated by Django 4.1.7 on 2023-03-24 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0003_alter_commentsmodel_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="commentsmodel",
            name="url",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="commentsmodel",
            name="date",
            field=models.DateTimeField(),
        ),
    ]