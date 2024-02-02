from django.db import models

# Create your models here.
class Education(models.Model):
    school_name = models.CharField(max_length=50)
    location  = models.CharField(max_length=100)
    degree_type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return f'[{self.school_name}, {self.location}, {self.degree_type}, {self.start_date}, {self.end_date}]'