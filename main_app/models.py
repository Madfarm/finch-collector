from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    species = models.CharField(max_length=100)
    mass = models.FloatField()
    sexual_dimorphism = models.BooleanField()

    def __str__(self):
       return f"{self.species} | mass: {self.mass} | sexually dimorphic: {self.sexual_dimorphism}"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})