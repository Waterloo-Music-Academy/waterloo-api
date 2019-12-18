# Generated by Django 3.0 on 2019-12-18 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0012_auto_20191218_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[(8, 'S'), (7, 'A+'), (6, 'A'), (5, 'B+'), (4, 'B'), (3, 'C'), (2, 'D'), (1, 'F')], default=1, max_length=2),
        ),
    ]
