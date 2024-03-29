from django.db import models

# Product model here
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    #Post w/r/t which the craic is being purchased, i.e., the recipient.
    

    def __str__(self):
        return self.name