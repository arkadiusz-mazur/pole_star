# Generated by Django 3.1.1 on 2020-09-21 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0001_position_ship'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='ship',
            name='date_added',
        ),
    ]
