# Generated by Django 2.1.5 on 2019-01-27 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20190127_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover_height',
            field=models.IntegerField(default=1600),
        ),
        migrations.AddField(
            model_name='album',
            name='cover_width',
            field=models.IntegerField(default=1600),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, height_field='cover_height', upload_to='album_imgs', width_field='cover_width'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='deans_list',
            field=models.BooleanField(default=False),
        ),
    ]
