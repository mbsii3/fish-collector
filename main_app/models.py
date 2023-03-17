from django.db import models
from django.urls import reverse

TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night')
)

class Decoration(models.Model):
    item = models.CharField(max_length=25)
    color = models.CharField(max_length=25)

    def __str__(self):
        return self.item
    
    def get_absolute_url(self):
        return reverse('decorations_detail', kwargs={'pk': self.id})

class Fish(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    water_type = models.CharField(max_length=100)
    decorations = models.ManyToManyField(Decoration)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'f_id': self.id})
    
class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    time = models.CharField(max_length=10, choices=TIMES, default=TIMES[0][0])

    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']