# Generated by Django 5.1.2 on 2024-11-04 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Awards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='awardcategory',
            name='year',
            field=models.IntegerField(default=2024),
        ),
    ]
