from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Mushroom(models.Model): 
  commonName = models.CharField(max_length=100)
  scientificName = models.CharField(max_length=100)
  description = models.TextField(max_length=500)

  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.commonName
  
  def get_absolute_url(self):
      return reverse("mushroom-detail", kwargs={"mushroom_id": self.pk})
  