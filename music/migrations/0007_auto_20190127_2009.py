# Generated by Django 2.1.5 on 2019-01-28 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20190127_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='album',
        ),
        migrations.RemoveField(
            model_name='label',
            name='album',
        ),
        migrations.AddField(
            model_name='album',
            name='genres',
            field=models.ManyToManyField(related_name='albums', to='music.Genre'),
        ),
        migrations.AddField(
            model_name='album',
            name='labels',
            field=models.ManyToManyField(related_name='albums', to='music.Label'),
        ),
        migrations.AddField(
            model_name='artist',
            name='genres',
            field=models.ManyToManyField(related_name='artists', to='music.Genre'),
        ),
        migrations.AddField(
            model_name='artist',
            name='labels',
            field=models.ManyToManyField(related_name='artists', to='music.Label'),
        ),
    ]