# Generated by Django 2.0.2 on 2018-02-08 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynewsfeed', '0005_remove_nytimespost_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuardianPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('url', models.CharField(blank=True, max_length=500)),
                ('trail_text', models.CharField(blank=True, max_length=1000)),
            ],
        ),
    ]
