# Generated by Django 2.0.3 on 2019-12-12 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comedia', '0002_auto_20191212_0400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='video_id',
        ),
    ]
