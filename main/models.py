from django.db import models

# Create your models here.
class Book(models.Model):
    autor=models.CharField(max_length=55)
    title=models.CharField(max_length=70)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    