from django.db import models
from django.urls import reverse

TYPES = (
    ('F', 'Fruits'),
    ('S','Seeds'),
    ('V','Vegetable')
)


# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=1, choices=TYPES)

    def __str__(self):
        return f" {self.name} | Type: {self.get_type_display()} "

class Finch(models.Model):
    species = models.CharField(max_length=100)
    mass = models.FloatField()
    sexual_dimorphism = models.BooleanField()
    foods = models.ManyToManyField(Food)

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