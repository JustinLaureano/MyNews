# Generated by Django 2.0.2 on 2018-02-08 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynewsfeed', '0003_nytimespost'),
    ]

    operations = [
        migrations.AddField(
            model_name='nytimespost',
            name='summary',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
