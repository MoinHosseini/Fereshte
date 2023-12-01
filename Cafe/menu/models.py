from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=127)
    price = models.IntegerField()
    description = models.TextField(max_length=1023)
    image = models.ImageField(upload_to='pics/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
