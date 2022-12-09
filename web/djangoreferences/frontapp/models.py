from django.db import models

class Heroes(models.Model):
    heroRole = models.CharField(max_length=15, blank=False)
    heroName = models.CharField(max_length=30, blank=False)
    strength = models.IntegerField(default=0)

    def __str__(self):
        return self.heroName
