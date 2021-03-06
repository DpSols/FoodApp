from django.db import models
from django.utils import timezone


# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    name = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='ingredients/')

    def __str__(self):
        return self.name


class Menu(models.Model):
    CATEGORY = (
        ('Main Dishes', 'Main Dishes'),
        ('Fast Food', 'Fast Food'),
        ('Thirst', 'Thirst'),
        ('Pasta', 'Pasta'),
        ('Appetizers', 'Appetizers'),
    )
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    ingredients = models.ManyToManyField(Ingredients)
    price = models.FloatField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='Menu/')

    def save(self, *args, **kwargs):
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out For Delivery', 'Out For Delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)
    menu = models.ForeignKey(Menu, null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.created_date


class Chief(models.Model):
    user = models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)
    dishes = models.ManyToManyField(Ingredients)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='chiefs/')

    def __str__(self):
        return self.user.name
