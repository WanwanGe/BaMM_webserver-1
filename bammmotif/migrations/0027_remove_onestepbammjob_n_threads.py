# Generated by Django 2.0.3 on 2018-04-16 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bammmotif', '0026_auto_20180416_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onestepbammjob',
            name='n_threads',
        ),
    ]
