# Generated by Django 3.0.3 on 2020-03-04 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20200304_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainsite.Room'),
        ),
    ]
