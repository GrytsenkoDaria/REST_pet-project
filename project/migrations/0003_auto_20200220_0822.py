# Generated by Django 3.0.2 on 2020-02-20 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20200213_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.IntegerField(choices=[(0, 'Created'), (1, 'Active'), (2, 'Paused'), (3, 'Closed')], default=0),
        ),
    ]
