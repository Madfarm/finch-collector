from django.db import models

# Create your models here.
class Finch(models.Model):
    species = models.CharField(max_length=100)
    mass = models.FloatField()
    sexual_dimorphism = models.BooleanField()

    def __str__(self):
       return f"{self.species} mass:{self.mass} sexually dimorphic:{self.sexual_dimorphism}"