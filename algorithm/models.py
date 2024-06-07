from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return self.username


class Property(models.Model):
    property_title = models.CharField(max_length=100)
    property_description = models.TextField()
    property_status = models.CharField(max_length=10, choices=[
        ('RENT', 'Rent'),
        ('SALE', 'Sale'),
    ])

    def __str__(self):
        return self.property_title


class PropertyPrice(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, primary_key=True)
    price = models.IntegerField()


class PropertyMedia(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')


class PropertyLocation(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)  # Consider precision for coordinates
    longitude = models.DecimalField(max_digits=10, decimal_places=6)


class PropertyExtraInfo(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField()
    bedroom = models.PositiveIntegerField()
    bathroom = models.PositiveIntegerField()
    property_type = models.CharField(max_length=20, choices=[
        ('HOUSE', 'House'),
        ('APARTMENT', 'Apartment'),
        ('LAND', 'Land'),
        ('COMMERCIAL', 'Commercial'),
        ('GARAGE', 'Garage'),
    ])
    area = models.DecimalField()  


class PropertyContact(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

class UserInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=20, choices=[
        ('VIEWED', 'Viewed'),
        ('SAVED', 'Saved'),
        ('RATED', 'Rated'),
    ])
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} interacted with {self.property.location} ({self.interaction_type})"