from django.db import models

# Create your models here.

class booking(models.Model):
    hname=models.TextField(max_length=1000)
    hprice=models.TextField(max_length=100)
    description=models.TextField(max_length=100)
    entered_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)


def __str__(self)->str:
    return self.hname