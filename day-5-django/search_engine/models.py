from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    hp = models.IntegerField(default=0)

    def __str__(self):
        return self.name
