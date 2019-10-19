# Generated by Django 2.2.5 on 2019-10-09 16:47

from django.db import migrations, models
import django.utils.crypto


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0012_auto_20191009_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='id',
            field=models.CharField(default=django.utils.crypto.get_random_string, editable=False, max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='artist',
            name='id',
            field=models.CharField(default=django.utils.crypto.get_random_string, editable=False, max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='genre',
            name='id',
            field=models.CharField(default=django.utils.crypto.get_random_string, editable=False, max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='label',
            name='id',
            field=models.CharField(default=django.utils.crypto.get_random_string, editable=False, max_length=8, primary_key=True, serialize=False),
        ),
    ]
