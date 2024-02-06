from django.db import models

# Create your models here.
class Award(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    def __str__(self):
        return f"[{self.title}, {self.year}]"