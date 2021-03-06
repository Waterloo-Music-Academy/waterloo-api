# Generated by Django 2.1.5 on 2019-01-27 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('music', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('S', 'S'), ('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], default='F', max_length=2)),
                ('standfirst', models.TextField()),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('album', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='music.Album')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
