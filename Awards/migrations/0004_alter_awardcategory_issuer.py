# Generated by Django 5.1.2 on 2024-11-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Awards', '0003_awardcategory_issuer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awardcategory',
            name='issuer',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
