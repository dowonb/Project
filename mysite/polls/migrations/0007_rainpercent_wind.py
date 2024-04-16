# Generated by Django 5.0.4 on 2024-04-16 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_remove_forecastdata_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rainpercent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fcstDate', models.CharField(max_length=8)),
                ('fcstTime', models.CharField(max_length=2)),
                ('fcstValue', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Wind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fcstDate', models.CharField(max_length=8)),
                ('fcstTime', models.CharField(max_length=2)),
                ('fcstValue', models.CharField(max_length=10)),
            ],
        ),
    ]