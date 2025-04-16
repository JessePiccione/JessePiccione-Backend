from django.db import models
from datetime import datetime 
class AwardCategory(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(default=datetime.now().year, null=True, blank=True)
    issuer = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return f"[{self.title}]"
    class Meta: 
        app_label = 'Awards'
class Award(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    category = models.ForeignKey(
        AwardCategory,
        related_name='awards',
        on_delete=models.PROTECT
    )
    def __str__(self):
        return f"[{self.title}, {self.year}]"
    class Meta: 
        app_label = 'Awards'

class Education(models.Model):
    school_name = models.CharField(max_length=50)
    location  = models.CharField(max_length=100)
    degree_type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return f'[{self.school_name}, {self.location}, {self.degree_type}, {self.start_date}, {self.end_date}]'
    class Meta:
        app_label = 'Education'