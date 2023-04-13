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
        return reverse('details', kwargs={'finch_id': self.id})
    
class Sighting(models.Model):
    location = models.CharField(max_length=30)
    date = models.DateField('Sighting Date')
    description = models.TextField(max_length=250)
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"Spotted at {self.location} on {self.date}"
    
    class Meta:
        ordering = ['-date']