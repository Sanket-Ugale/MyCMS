from django.db import models
from tinymce.models import HTMLField
# from autoslug import AutoSlugField 
class blog(models.Model):
    Title=models.CharField(max_length=100)
    date=models.DateField(("Date"), auto_now=False, auto_now_add=False)
    author=models.CharField(max_length=90)
    category=models.CharField(max_length=90)
    description=models.TextField( max_length=400)
    url=models.CharField(unique=True, max_length=100)
    banner=models.ImageField(upload_to="images/", height_field=None, width_field=None, max_length=None)
    content=HTMLField()
# Create your models here.
