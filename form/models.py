from django.db import models
class form(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.CharField( max_length=40)
    Subject=models.CharField(max_length=100)
    Message=models.TextField(max_length=500)
    

    # def __str__(self):
    #     return 

    # def __unicode__(self):
    #     return 

# Create your models here.
