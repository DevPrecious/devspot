# Generated by Django 3.0.5 on 2020-05-26 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devspot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='DevSpot', max_length=50),
        ),
    ]
