from django.db import models
from datetime import datetime 
class AwardCategory(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(default=datetime.now().year)
    issuer = models.CharField(max_length=255, default=None)
    def __str__(self):
        return f"[{self.title}]"
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