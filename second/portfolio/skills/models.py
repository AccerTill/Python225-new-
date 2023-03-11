from django.db import models

# Create your models here.

# ID создался автоматически:

class Skills(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='part_2/images/')
    url = models.URLField(blank=True)



    def __str__(self):
        return self.title














