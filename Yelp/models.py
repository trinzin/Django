from django.db import models

class Food(models.Model):
    name= models.CharField(max_length = 200)
    description = models.CharField(max_length = 300)
    price = models.FloatField(default =0)
    image = models.ImageField(upload_to='food_images/')
    summary = models.CharField(max_length = 200)

    def __str__(self):
        return self.summary
