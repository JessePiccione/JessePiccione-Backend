# Generated by Django 5.0 on 2024-04-14 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkExperience', '0002_workexperience_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='description',
            field=models.CharField(max_length=511),
        ),
    ]