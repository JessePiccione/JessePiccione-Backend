from django.db import models

# Create your models here.
class SkillCategory(models.Model):
    category_name = models.CharField(max_length=255)
    def __str__(self):
        return f'[{self.category_name}]'
class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        SkillCategory,
        related_name='skills',
        on_delete = models.PROTECT
    )
    def __str__(self):
        return f'[{self.name}, {self.category}]'