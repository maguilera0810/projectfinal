# Generated by Django 2.0.3 on 2019-12-12 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('firstname', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=64, unique=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('comment', models.CharField(max_length=300, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comedia.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=604)),
                ('url', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='video_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comedia.Video'),
        ),
    ]
