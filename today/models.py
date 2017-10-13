from django.db import models


class Celebrate(models.Model):
    date = models.DateField()
    label = models.TextField()

