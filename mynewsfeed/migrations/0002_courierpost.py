# Generated by Django 2.0.2 on 2018-02-07 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynewsfeed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourierPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('url', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]
