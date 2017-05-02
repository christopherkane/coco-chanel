from django.db import modelso

class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)i
