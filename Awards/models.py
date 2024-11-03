from django.db import models

class AwardCategory(models.Model):
    title = models.CharField
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