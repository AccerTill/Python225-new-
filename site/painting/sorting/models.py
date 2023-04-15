from django.db import models

# Create your models here.

class Sorting(models.Model):
    name = models.CharField(max_length=100)
    genre_author = models.CharField(max_length=500)
    picture = models.ImageField(upload_to ='sorting/images/')
    links = models.URLField(blank=True)  # -----links



    def __str__(self):
        return self.name




