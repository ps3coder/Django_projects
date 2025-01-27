from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,unique=True)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200,blank=True)
    position = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name