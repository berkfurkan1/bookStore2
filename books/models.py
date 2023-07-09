from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField('date created')
    def __str__(self) :
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField('date created')
    author =models.ForeignKey(Author, on_delete=models.CASCADE)
    #models.CASCADE -> bir yazar silindiğinde yazara ait kitapları siler. 
    price = models.DecimalField(decimal_places=2,max_digits=4,null=True)
    
    def __str__(self) :
        return self.name