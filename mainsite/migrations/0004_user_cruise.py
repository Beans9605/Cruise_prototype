# Generated by Django 3.0.3 on 2020-03-05 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_auto_20200304_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cruise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainsite.Cruise'),
        ),
    ]