from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class User(AbstractUser):
    
    def __str__(self):
        return self.username
    
class Property(models.Model):
    property_title = models.CharField(max_length=100)
    property_description = models.TextField()
    property_status = models.CharField(choices=[
        ('RENT', 'Rent'),
        ('SALE', 'Sale'),
    ])
    
class PropertyPrice(models.Model):
    property = models.OneToOneField(property, on_delete=models.CASCADE, primary_key=True)
    price = models.IntegerField()
    
class PropertyMedia(models.Model):
    property = models.ForeignKey(property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images')
    
class PropertyLocation(models.Model):
    property = models.OneToOneField(property, on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.DecimalField()
    longitude = models.DecimalField()
    
class PropertyExtraInfo(models.Model):
    property = models.OneToOneField(property, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField()
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    type = models.CharField(choices=[
        ('HOUSE', 'House'),
        ('APARTMENT', 'Apartment'),
        ('LAND', 'Land'),
        ('COMMERCIAL', 'Commercial'),
        ('GARAGE', 'Garage'),
    ])
    area = models.IntegerField()
    
class PropertyContact(models.Model):
    property = models.OneToOneField(property, on_delete=models.CASCADE)
    name = models.CharField()
    email = models.EmailField()
    phone = models.CharField()
    