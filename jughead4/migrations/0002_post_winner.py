# Generated by Django 2.2.12 on 2020-06-07 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jughead4', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='winner',
            field=models.BooleanField(default=0),
        ),
    ]
