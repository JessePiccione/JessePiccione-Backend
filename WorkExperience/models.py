from django.db import models

class WorkExperience(models.Model):
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    title_held = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=511)
    def __str__(self):
        return f'[{self.company_name}, {self.location}, {self.title_held}, {self.start_date}, {self.end_date}, {self.description}]'