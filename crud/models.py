from django.db import models

# Create your models here.
class Employee(models.Model):
    name= models.CharField(max_length=200)
    age=models.IntegerField()
    email=models.EmailField()
    message=models.TextField()
    number=models.CharField(max_length=10,null=True)
    is_deleted = models.BooleanField(default=False)