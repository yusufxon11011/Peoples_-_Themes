from django.db import models

class Weekday(models.Model):
    name_uz = models.CharField(max_length=20)
    name_en = models.CharField(max_length=20)
    name_ru = models.CharField(max_length=20)

    def __str__(self):
        return self.name_uz
