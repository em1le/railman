# Generated by Django 4.1.6 on 2023-02-11 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kilometerpoint',
            options={'verbose_name': 'Point Kilometrique', 'verbose_name_plural': 'Points Kilometriques'},
        ),
        migrations.AddField(
            model_name='kilometerpoint',
            name='description',
            field=models.CharField(default='', max_length=140, verbose_name='Description du Point Kilometrique'),
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.CharField(default='', max_length=140, verbose_name='Description du projet'),
        ),
        migrations.AddField(
            model_name='route',
            name='description',
            field=models.CharField(default='', max_length=140, verbose_name='Description du trajet'),
        ),
        migrations.AddField(
            model_name='track',
            name='description',
            field=models.CharField(default='', max_length=140, verbose_name='Description de la voie'),
        ),
    ]