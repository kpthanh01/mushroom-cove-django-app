from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Mushroom(models.Model): 
  name = models.CharField(max_length=100)
  scientific = models.CharField(max_length=100)
  description = models.TextField(max_length=500)

  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("mushroom-detail", kwargs={"mushroom_id": self.pk})

class Tracking(models.Model):
  title = models.CharField(max_length=50)
  date = models.DateField('Tracking Date')
  notes = models.CharField(max_length=500)
  location = models.CharField(max_length=100)

  mushroom = models.ForeignKey(Mushroom, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.date}"

  class Meta:
    ordering = ['-date']
