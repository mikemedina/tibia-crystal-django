from django.db import models


class Spell(models.Model):
    name = models.CharField(max_length=255)
    vocation = models.CharField(max_length=255)
    x_max = models.FloatField()
    y_max = models.IntegerField()
    x_min = models.FloatField()
    y_min = models.IntegerField()
    target_cap = models.IntegerField()

    def __str__(self):
        return self.name
