from django.db import models

# Create your models here.

class Part_2(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    pictures = models.ImageField(upload_to ='part_2/images/')
    links = models.URLField(blank=True)  # -----links











