from django.db import models

# Create your models here.

"""
Product 
-NOM 
-PRIX
-La quantité en stock 
-Description 
-image 

"""

class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price=models.FloatField(default=0.0)
    stock=models.IntegerField(default=0)
    description=models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products",blank=True,null=True)
     #blank et null egale a true pour ne pas forcer l'utilisateur a mettre une photo 
    def __str__(self) :
        return f"{self.name}({self.stock})"
                                                                                 
    
