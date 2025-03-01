from django.db import models

# Create your models here.
class Message(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, default='')
    subject = models.CharField(max_length=255)
    message = models.TextField()
    def __str__(self):
        return f'[{self.email}, {self.name}, {self.subject}, {self.message}]'
    