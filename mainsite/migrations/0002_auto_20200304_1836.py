# Generated by Django 3.0.3 on 2020-03-04 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_passenger',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_sailer',
            field=models.BooleanField(default=False),
        ),
    ]
