from django.db import models
class commentsModel(models.Model):
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=90)
    url=models.CharField(max_length=200)
    date=models.DateTimeField()
    message=models.TextField()


# Create your models here.
