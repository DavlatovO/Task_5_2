from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100)
    population = models.PositiveIntegerField()
    area = models.FloatField()
    picture = models.ImageField(upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.name

