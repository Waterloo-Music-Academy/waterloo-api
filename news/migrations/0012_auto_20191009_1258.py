# Generated by Django 2.2.5 on 2019-10-09 17:58

from django.db import migrations, models
import django.utils.crypto


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20191009_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.CharField(default=django.utils.crypto.get_random_string, editable=False, max_length=8, primary_key=True, serialize=False),
        ),
    ]
