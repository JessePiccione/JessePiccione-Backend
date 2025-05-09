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
# Create your models here.


class Message(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, default='')
    subject = models.CharField(max_length=255)
    message = models.TextField()
    def __str__(self):
        return f'[{self.email}, {self.name}, {self.subject}, {self.message}]'
    class Meta: 
        app_label = 'Message'

class Project(models.Model):
    name = models.CharField(max_length=100)
    sponser = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    contribution = models.CharField(max_length=1028)
    def __str__(self):
        return f'[{self.name}, {self.sponser}, {self.start_date}, {self.end_date}, {self.contribution}]'
    class Meta:
        app_label = 'Projects'

class HomePageEntry(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    URL = models.URLField()
    def __str__(self):
        return self.title
    class Meta: 
        app_label = 'Resume'
class Technology(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    pageEntry = models.ForeignKey(
        HomePageEntry,
        related_name='technologies',
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.title
    class Meta: 
        app_label='Resume'
class SkillCategory(models.Model):
    category_name = models.CharField(max_length=255)
    def __str__(self):
        return f'[{self.category_name}]'
    class Meta:
        app_label='Skills'
class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        SkillCategory,
        related_name='skills',
        on_delete = models.PROTECT
    )
    def __str__(self):
        return f'[{self.name}, {self.category}]'
    class Meta:
        app_label='Skills'


class WorkExperience(models.Model):
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    title_held = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=511)
    def __str__(self):
        return f'[{self.company_name}, {self.location}, {self.title_held}, {self.start_date}, {self.end_date}, {self.description}]'
    class Meta:
        app_label = 'WorkExperience'