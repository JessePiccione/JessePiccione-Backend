from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    sponser = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    contribution = models.CharField(max_length=255)
    def __str__(self):
        return f'[{self.name}, {self.sponser}, {self.start_date}, {self.end_date}, {self.contribution}]'
