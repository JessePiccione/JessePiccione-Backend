from django.db import models

# Create your models here.
class HomePageEntry(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    URL = models.URLField()
    def __str__(self):
        return self.title
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