from django.db import models

class Pupil(models.Model):
    name = models.CharField(max_length=100)
    grades = models.TextField()